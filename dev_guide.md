
## mathscr

目前默认的`\mathscr`是`mathalpha`提供的 boondoxo 字体。要使用 rsfs 的话可以用 `\mathrsfs`. ([pr56](https://github.com/NominHanggai/szaboqc/pull/56))

## autoref

尽量用 `\autoref` 来引用图表和公式，其引用章节、方程、图、表时自动写成“第……章（节）”、“式(x.y)”、“图x.y”、“表x.y”这样的样式。
详见[pr21](https://github.com/NominHanggai/szaboqc/pull/21).

## 公式编号

(2.3a)(2.3b) 之类的编号用 `subequations` 实现。参见[pr17](https://github.com/NominHanggai/szaboqc/pull/17).

我们希望翻译版的公式编号和原书一一对应。

## 上波浪线

在书写带有上波浪线的符号时，使用 `\widetilde{}` $\widetilde{\Psi}$ 而不是 `\tilde{}` $\tilde{\Psi}$，以获得更好的显示效果。

## 希腊字母加粗

**在数学环境下**，如果要加粗希腊字母，避免使用 `\boldsymbol{}`，应当使用 `\mathbf{}` 或者便捷方式 `\mbf{}`。由于字体原因，LaTeX 会自动将希腊字母的 `\boldsymbol{}` 转为 `\mathbf{}` 字体。

## 带有数学环境的章节名（书签）

如果章节名中有数学环境，为了在生成的 PDF 书签中正确显示章节名，需要使用 `\texorpdfstring{<TeX内容>}{<PDF书签内容>}`，其中 `<PDF书签内容>` 是纯文本内容，不含数学环境。例如 H₂ 应写为 `\texorpdfstring{H$_2$}{H₂}`。
