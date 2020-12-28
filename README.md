# Modern Quantum Chemistry 现代量子化学 汉化版
Attila Szabo & Neil Ostlund *Modern Quantum Chemistry: Introduction to Advanced Electronic Structure Theory* 中文翻译。重新绘制了所有插图。

Tex Live 2020 下 XeLaTeX编译成功。CTeX需更新至v2.5.1。

Tikz插图用 tikz/external 库导出到了 ./tikz 中。修改或添加图片后，编译时需用 xelatex -shell-escape 以便使用 external 库的 system call。不妨一直带着 -shell-escape (本文档没有危险)。

如果编译后引用失效则可能需要使用xelatex再编译一次。