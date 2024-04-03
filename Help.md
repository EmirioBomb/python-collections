
# 帮助文档
## 项目初始化
> 项目初始化时，需创建 **.version.json** 与  **.gitignore**

<details>
<summary>.version.json</summary>

```json
{
    "types": [
        {
            "type": "feat",
            "section": "✨ 新功能"
        },
        {
            "type": "fix",
            "section": "🐛 问题修复"
        },
        {
            "type": "init",
            "section": "🎉 初始化"
        },
        {
            "type": "docs",
            "section": "📝 文档"
        },
        {
            "type": "style",
            "section": "🎨 风格"
        },
        {
            "type": "refactor",
            "section": "♻️ 代码重构"
        },
        {
            "type": "perf",
            "section": "⚡ 性能优化"
        },
        {
            "type": "test",
            "section": "✅ 测试"
        },
        {
            "type": "revert",
            "section": "⏪ 版本回退",
        },
        {
            "type": "build",
            "section": "📦‍ 构建"
        },
        {
            "type": "chore",
            "section": "🚀 项目依赖"
        },
        {
            "type": "ci",
            "section": "👷 CI"
        }
    ]
}
```

</details>

<details>
<summary>.gitignore</summary>

```txt
# macos
.DS_Store
.AppleDouble
.LSOverride

# visual studio code
.vscode/*
```

</details>


## 提交流程

```bash
# 1. 测试版本变更信息
$ standard-version -s -a -t 'python-collections-v' --dry-run

# 2. 手动替换README.md版本号如： -v1.0.1-  >  -v1.0.2-
# 3. 提交版本号改动，类型为: docs，内容为: 更新版本号及变更日志内容

# 4. 更新changelog，并tag
$ standard-version -s -a -t 'python-collections-v'

# 5. 推送tag
$ git push --follow-tags

# 6. release发版
```