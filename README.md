# 库林量价分析学习技能

基于安娜·库林《量价分析：量价分析创始人威科夫的盘口解读方法》（*A Complete Guide to Volume Price Analysis*）生成的Agent Skill，使用 [book-to-skill](https://github.com/virgiliojr94/book-to-skill) 提取结构。面向学习方法与分析用户提供的图表，涵盖威科夫三定律、量价异常、供需测试、突破回测、动态支点、多周期和VAP。

内容是综合改写的学习框架，不是原书文本。仓库不含原始EPUB、全文提取、原书插图或大段引用。12张关键图表仅用于核对，核对记录见 [provenance.md](provenance.md)。

## 安装与调用

仓库公开发布于GitHub账号 `Charles666AI` 下。

```sh
npx skills add https://github.com/Charles666AI/coulling-volume-price-analysis --skill coulling-volume-price-analysis
```

也可将整个技能目录放到支持Agent Skills的主机技能目录，例如 `~/.agents/skills/coulling-volume-price-analysis/`。根目录必须保留 `SKILL.md` 以及它引用的文件。

示例请求：

> 使用 coulling-volume-price-analysis，教我第5章供给测试。先出一道练习，等我回答再解析。

> 使用 coulling-volume-price-analysis，分析这张量价图。分别给出事实、主解释、竞争解释、确认和失效条件。

> 使用 coulling-volume-price-analysis，复盘我的判断，检查有没有使用未来支点。

## 独立仓库结构

```text
coulling-volume-price-analysis/
├── SKILL.md                 # 核心框架、调用流程、章节及主题索引
├── chapters/                # 12章，按需读取
├── glossary.md              # 术语定义
├── patterns.md              # 适用条件、操作与取舍
├── cheatsheet.md            # 快速判断表
├── examples/
│   ├── analysis-template.md # 证据、情景与复盘模板
│   ├── synthetic-breakout.md# 合成OHLCV及失败分支
│   └── study-plan.md        # 七次学习练习
├── tools/check_package.py   # 链接、文件结构与内容边界检查
├── provenance.md            # 来源、覆盖与图表核对
├── COPYRIGHT.md             # 来源权利与分享边界
├── README.md
└── .gitignore
```

无需复制转换器运行时，无需依赖原书路径。技能是Markdown资料；辅助检查脚本只需Python标准库：

```sh
python tools/check_package.py
```

## 阅读方式与限制

主文件先给核心框架，相关章节按问题加载。每章包含适用条件、操作、关键概念、心智模型、反模式、重构例子及连接。例子标注了原书推理重构与本技能新建的合成练习。

作者2013年的平台、产品与“最新发展”不能当作今天的事实；本技能不提供经过回测的胜率或收益承诺。书中对局内人的描述作为解释模型使用，不能凭OHLCV认定主体身份。对于实时行情或现实投资决策，应另行核验当前数据与规则。
