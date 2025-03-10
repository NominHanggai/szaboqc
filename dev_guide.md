
## mathscr

目前默认的`\mathscr`是`mathalpha`提供的 boondoxo 字体。要使用 rsfs 的话可以用 `\mathrsfs`. ([pr56](https://github.com/NominHanggai/szaboqc/pull/56))

## autoref

尽量用 `\autoref` 来引用图表和公式，其引用章节、方程、图、表时自动写成“第……章（节）”、“式(x.y)”、“图x.y”、“表x.y”这样的样式。
详见[pr21](https://github.com/NominHanggai/szaboqc/pull/21).

## 公式编号

(2.3a)(2.3b) 之类的编号用 `subequations` 实现。参见[pr17](https://github.com/NominHanggai/szaboqc/pull/17).

我们希望翻译版的公式编号和原书一一对应。