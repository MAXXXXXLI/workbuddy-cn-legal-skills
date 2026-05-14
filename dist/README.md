# WorkBuddy 直导包

本目录下的 `workbuddy-skill-zips/` 包含 `151` 个可供 WorkBuddy 单独导入的 skill zip。

WorkBuddy v4.22.11 上传 zip 时要求 `SKILL.md` 位于 zip 顶层，因此请导入这里的单 skill zip，例如：

```text
workbuddy-skill-zips/commercial-legal--nda-review.zip
```

不要上传仓库根目录 zip，也不要上传旧的模块整包 zip；这类 zip 的 `SKILL.md` 不在顶层，WorkBuddy 会提示 `SKILL.md not found in zip archive`。

zip 文件名保留英文稳定标识，便于更新；WorkBuddy 中显示的 `name` 已改为中文，例如 `商事合同法务-保密协议审查`。

在仓库根目录整体导入全部 skills：

```bash
bash scripts/install_all_workbuddy_skills.sh
```

覆盖更新已有安装：

```bash
bash scripts/install_all_workbuddy_skills.sh --force
```
