package de.rampro.activitydiary.ui.generic;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import com.google.gson.Gson;
import com.squareup.picasso.Picasso;

import de.rampro.activitydiary.R;
import de.rampro.activitydiary.base.ContentURL;
import de.rampro.activitydiary.bean.HistoryDescBean;

public class HistoryDescActivity extends BaseActivity implements View.OnClickListener {

    private ImageView backIv, shareIv, picIv;
    private TextView titleTv;
    private TextView contentTv;
    private String hisId;
    HistoryDescBean.ResultBean resultBean;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_history_desc);
        backIv = (ImageView) findViewById(R.id.desc_back_iv);
        shareIv = (ImageView) findViewById(R.id.desc_share_iv);
        picIv = (ImageView) findViewById(R.id.desc_iv_pic);
        titleTv = (TextView) findViewById(R.id.desc_tv_title);
        contentTv = (TextView) findViewById(R.id.desc_tv_content);
        backIv.setOnClickListener(this);
        shareIv.setOnClickListener(this);

        hisId = getIntent().getStringExtra("hisId");
        String historyDescURL = ContentURL.getHistoryDescURL("1.0", hisId);
        loadData(historyDescURL);

    }

    @Override
    public void onSuccess(String result) {
        HistoryDescBean bean = new Gson().fromJson(result, HistoryDescBean.class);
        resultBean = bean.getResult().get(0);
        titleTv.setText(resultBean.getTitle());
        contentTv.setText(resultBean.getContent());
        String picUrl = resultBean.getPic();
        if (TextUtils.isEmpty(picUrl)) {
            picIv.setVisibility(View.GONE);
        } else {
            picIv.setVisibility(View.VISIBLE);
            // Picasso.with(this).load(picUrl).into(picIv);
            Picasso.get().load(picUrl).into(picIv);
        }
    }

    @Override
    public void onClick(View v) {
        if (v.getId() == R.id.desc_back_iv) {
            finish();
        } else if (v.getId() == R.id.desc_share_iv) {
            String text = "我发现一款好用的软件-ActivityDiary，快来一起探索这个APP吧！";
            if (resultBean != null) {
                text = "想要了解" + resultBean.getTitle() + "详情么？快来下载ActivityDiaryApp吧！";
            }
            Intent intent = new Intent(Intent.ACTION_SEND);
            intent.setType("text/plain");
            intent.putExtra(Intent.EXTRA_TEXT, text);
            startActivity(Intent.createChooser(intent, "ActivityDiary"));
        }
    }
}
