# FLZT 每日签到

## 使用说明

使用 GitHub Actions 实现定时任务

1. Fork 本项目

2. 添加 Secrets

   方法：Settings -> Secrets -> New repository secret

    - BASE_URL (`https://flzt.top`，必填)
    - EMAIL (邮箱，必填)
    - PASSWORD (密码，必填)
    - SERVER_KEY ([Server酱](https://sct.ftqq.com/sendkey) SendKey，用于推送脚本执行结果；选填)

3. 修改 `.github/workflows` 定时策略

   参考 GitHub Actions 文档 [CRON](https://docs.github.com/zh/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#schedule)

    ```yml
    schedule:
        - cron: '0 6 * * *'
    ```

## 免责声明

本代码仅用于学习，下载后请勿用于商业用途，并且使用该脚本发生的一切后果与本人无关。
