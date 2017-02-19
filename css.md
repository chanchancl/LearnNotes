
# CSS

请注意，阅读这篇文章，你不可避免的会遇到 `CSS` `HTML` 等相关知识。


## 选择器

选择器是一种可以帮助你**快速定位元素**的工具，定位之后可以对这些元素进行样式的设定

### 1.基本选择器
    .selector {
        property: value
    }

    h1 {
        color:red;
         font-size:14px;
    }

### 2.派生选择器
    li strong {
        font-style: italic;
        font-weight: normal;
    }
    
li 中的 strong 标签

    <p>
        <strong>我是粗体字，不是斜体字，因为我不在列表当中，所以这个规则对我不起作用</strong>
    </p>
    
    <ol>
        <li><strong>我是斜体字。这是因为 strong 元素位于 li 元素内。</strong></li>
        <li>我是正常的字体。</li>
    </ol>


### 3.id选择器

    #red {
        color:red; 
    }
    <p id="red">这个段落是红色。</p>
    <p id="green">这个段落是绿色。</p>


基于id的 派生选择器

    #red p{ }

### 4. 类选择器

    .center {
        text-align: center;
    }


    <h1 class="center">
        This heading will be center-aligned
    </h1>

    <p class="center">
        This paragraph will also be center-aligned.
    </p>

基于类的派生选择器

    .fancy td {
        color: #f60;
        background: #666;
    }


### 5.属性选择器
这个是新语法。。。
对带有指定属性的HTML元素设置样式

为带有 title 属性的所有元素设置样式

    [title]
    {
        color:red;
    }

## 二 创建CSS

### 1.外部样式表
当样式需要应用于很多页面时，外部样式表将是理想的选择。在使用外部样式表的情况下，你可以通过改变一个文件来改变整个站点的外观。每个页面使用 <link> 标签链接到样式表。<link> 标签在（文档的）头部：

    <head>
    <link rel="stylesheet" type="text/css" href="mystyle.css" />
    </head>

### 2.内部样式表

    <head>
        <style type="text/css">
            hr {color: sienna;}
            p {margin-left: 20px;}
            body {background-image: url("images/back40.gif");}
        </style>
    </head>

### 3.内联样式
由于要将表现和内容混杂在一起，内联样式会损失掉样式表的许多优势。请慎用这种方法，例如当样式仅需要在一个元素上应用一次时。
要使用内联样式，你需要在相关的标签内使用样式（style）属性。Style 属性可以包含任何 CSS 属性。本例展示如何改变段落的颜色和左外边距：
    
    <p style="color: sienna; margin-left: 20px">
        This is a paragraph
    </p>


元素的最终样式，优先取自 内联样式 >  内部样式 > 外联样式

## 三 CSS样式

### 1.背景

#### (1)背景色： background-color 属性

    p { background-color: gray; }

如果希望背景色从元素中的文本向外少有延伸，需增加一些内边距：

    p {
        background-color: gray;
        padding: 20px;
    }

`background-color` 不能继承，其默认值是 `transparent`。`transparent` 有“透明”之意。也就是说，如果一个元素没有指定背景色，那么背景就是透明的，这样其祖先元素的背景才能可见。

#### (2)背景图像

    body { background-image: url(/i/eg_bg_04.gif); }

如果需要在页面上对背景图像进行平铺，可以使用 `background-repeat` 属性。

    body { 
      background-image: url(/i/eg_bg_03.gif);
      background-repeat: repeat-y;
    }

可以利用 background-position 属性改变图像在背景中的位置。
在 body 元素中将一个背景图像居中放置：

    body { 
        background-image:url('/i/eg_bg_03.gif');
        background-repeat:no-repeat;
        background-position:center;
    }

#### 背景关联
如果文档比较长，那么当文档向下滚动时，背景图像也会随之滚动。当文档滚动到超过图像的位置时，图像就会消失。
可以通过 `background-attachment` 属性防止这种滚动。通过这个属性，可以声明图像相对于可视区是固定的（fixed），因此不会受到滚动的影响：

    body {
        background-image:url(/i/eg_bg_02.gif);
        background-repeat:no-repeat;
        background-attachment:fixed
    }

  
### 2.文本

#### (1)缩进文本
把 Web 页面上的段落的第一行缩进，这是一种最常用的文本格式化效果。
CSS 提供了 `text-indent` 属性，该属性可以方便地实现文本缩进。
通过使用 text-indent 属性，所有元素的第一行都可以缩进一个给定的长度，甚至该长度可以是负值。
这个属性最常见的用途是将段落的首行缩进，下面的规则会使所有段落的首行缩进` 5 em`：

    p { text-indent: 5em; }

**使用负值**
text-indent 还可以设置为负值。利用这种技术，可以实现很多有趣的效果，比如“悬挂缩进”，即第一行悬挂在元素中余下部分的左边：

    p { text-indent: -5em; } 

不过在为 text-indent 设置负值时要当心，如果对一个段落设置了负值，那么首行的某些文本可能会超出浏览器窗口的左边界。为了避免出现这种显示问题，建议针对负缩进再设置一个外边距或一些内边距：

    p {
        text-indent: -5em; 
        padding-left: 5em;
    }

**使用百分比值**
text-indent 可以使用所有长度单位，包括百分比值。
百分数要相对于缩进元素父元素的宽度。换句话说，如果将缩进值设置为 20%，所影响元素的第一行会缩进其父元素宽度的 20%。
在下例中，缩进值是父元素的 20%，即 100 个像素：

    div {width: 500px;}
    p {text-indent: 20%;}

    <div>
        <p>this is a paragragh</p>
    </div>

**继承**
text-indent 属性可以继承，请考虑如下标记：

    div #outer {width: 500px;}
    div #inner {text-indent: 10%;}
    p {width: 200px;}

    <div id="outer">
        <div id="inner">some text. some text. some text.
            <p>this is a paragragh.</p>
        </div>
    </div>
以上标记中的段落也会缩进 50 像素，这是因为这个段落继承了 id 为 inner 的 div 元素的缩进值。



#### (2)水平对齐
`text-align` 是一个基本的属性，它会影响一个元素中的文本行互相之间的对齐方式。它的前 3 个值相当直接，不过第 4 个和第 5 个则略有些复杂。
值 left、right 和 center 会导致元素中的文本分别左对齐、右对齐和居中。

最后一个水平对齐属性是 `justify`。
在两端对齐文本中，文本行的左右两端都放在父元素的内边界上。然后，调整单词和字母间的间隔，使各行的长度恰好相等。两端对齐文本在打印领域很常见。



#### (3)字间隔

`word-spacing` 属性可以改变字（单词）之间的标准间隔。其默认值 normal 与设置值为 0 是一样的。
word-spacing`属性接受一个正长度值或负长度值。如果提供一个正长度值，那么字之间的间隔就会增加。为 `word-spacing` 设置一个负值，会把它拉近：
   
    p.spread {word-spacing: 30px;}
    p.tight {word-spacing: -0.5em;}

    <p class="spread">
        This is a paragraph. The spaces between words will be increased.
    </p>

    <p class="tight">
        This is a paragraph. The spaces between words will be decreased.
    </p>


#### (4)字母间隔

`letter-spacing` 属性与 word-spacing 的区别在于，字母间隔修改的是字符或字母之间的间隔。
与 word-spacing 属性一样，letter-spacing 属性的可取值包括所有长度。默认关键字是 normal（这与 letter-spacing:0 相同）。输入的长度值会使字母之间的间隔增加或减少指定的量：

    h1 {letter-spacing: -0.5em}
    h4 {letter-spacing: 20px}

    <h1>This is header 1</h1>
    <h4>This is header 4</h4>


#### (5)字符转换
`text-transform` 属性处理文本的大小写。这个属性有 4 个值：
* none
* uppercase
* lowercase
* capitalize

默认值 none 对文本不做任何改动，将使用源文档中的原有大小写。

uppercase 和 lowercase 将文本转换为全大写和全小写字符。

capitalize 只对每个单词的首字母大写。

作为一个属性，text-transform 可能无关紧要，不过如果您突然决定把所有 h1 元素变为大写，这个属性就很有用。不必单独地修改所有 h1 元素的内容，只需使用 text-transform 为你完成这个修改：

    h1 {text-transform: uppercase}


#### (6)文本装饰
`text-decoration` 属性，这是一个很有意思的属性，它提供了很多非常有趣的行为。
text-decoration 有 5 个值：
* none
* underline
* overline
* line-through
* blink

 underline 会对元素加下划线，就像 HTML 中的 U 元素一样。

 overline 的作用恰好相反，会在文本的顶端画一个上划线。
 
 值 line-through 则在文本中间画一个贯穿线，等价于 HTML 中的 S 和 strike 元素。
 
 blink 会让文本闪烁，类似于 Netscape 支持的颇招非议的 blink 标记。

#### (7)处理空白符
`white-space` 属性会影响到用户代理对源文档中的空格、换行和 tab 字符的处理。
通过使用该属性，可以影响浏览器处理字之间和文本行之间的空白符的方式。从某种程度上讲，默认的 XHTML 处理已经完成了空白符处理：它会把所有空白符合并为一个空格。所以给定以下标记，它在 Web 浏览器中显示时，各个字之间只会显示一个空格，同时忽略元素中的换行：
    
    <p>This     paragraph has    many
        spaces           in it.</p>

可以用以下声明显式地设置这种默认行为：
    
    p {white-space: normal;}

值 pre
不过，如果将 white-space 设置为 pre ，受这个属性影响的元素中，空白符的处理就有所不同，其行为就像 XHTML 的 pre 元素一样；空白符不会被忽略。
如果 white-space 属性的值为 pre ，浏览器将会注意额外的空格，甚至回车。在这个方面，而且仅在这个方面，任何元素都可以相当于一个 pre 元素。


#### (8)文本方向

`direction` 属性影响块级元素中文本的书写方向、表中列布局的方向、内容水平填充其元素框的方向、以及两端对齐元素中最后一行的位置。


direction 属性有两个值：ltr 和 rtl。大多数情况下，默认值是 ltr，显示从左到右的文本。如果显示从右到左的文本，应使用值 rtl。



### 3.字体

在 CSS 中，有两种不同类型的字体系列名称：
通用字体系列 - 拥有相似外观的字体系统组合（比如 "Serif" 或 "Monospace"）
特定字体系列 - 具体的字体系列（比如 "Times" 或 "Courier"）
除了各种特定的字体系列外，CSS 定义了 5 种通用字体系列：

* Serif 字体
* Sans-serif 字体
* Monospace 字体
* Cursive 字体
* Fantasy 字体


#### (1)指定字体系列
使用 `font-family` 属性 定义文本的字体系列。

使用通用字体系列

如果你希望文档使用一种 sans-serif 字体，但是你并不关心是哪一种字体，以下就是一个合适的声明：
    
    body {font-family: sans-serif;}

这样用户代理就会从 sans-serif 字体系列中选择一个字体（如 Helvetica），并将其应用到 body 元素。因为有继承，这种字体选择还将应用到 body 元素中包含的所有元素，除非有一种更特定的选择器将其覆盖。


指定字体系列

除了使用通用的字体系列，您还可以通过 font-family 属性设置更具体的字体。
下面的例子为所有 h1 元素设置了 Georgia 字体：

    h1 {font-family: Georgia;}

#### (2)字体风格
`font-style` 属性最常用于规定斜体文本。
该属性有三个值：
normal - 文本正常显示
italic - 文本斜体显示
oblique - 文本倾斜显示

in css:

    p.normal {font-style:normal;}
    p.italic {font-style:italic;}
    p.oblique {font-style:oblique;}


#### (3)字体加粗
`font-weight` 属性设置文本的粗细。
使用 bold 关键字可以将文本设置为粗体。

关键字 100 ~ 900 为字体指定了 9 级加粗度。如果一个字体内置了这些加粗级别，那么这些数字就直接映射到预定义的级别，100 对应最细的字体变形，900 对应最粗的字体变形。数字 400 等价于 normal，而 700 等价于 bold。

如果将元素的加粗设置为 bolder，浏览器会设置比所继承值更粗的一个字体加粗。与此相反，关键词 lighter 会导致浏览器将加粗度下移而不是上移。

实例

    p.normal {font-weight:normal;}
    p.thick {font-weight:bold;}
    p.thicker {font-weight:900;}


#### (4)字体大小
`font-size` 属性设置文本的大小。

有能力管理文本的大小在 web 设计领域很重要。但是，您不应当通过调整文本大小使段落看上去像标题，或者使标题看上去像段落。
请始终使用正确的 HTML 标题，比如使用 `<h1> - <h6>` 来标记标题，使用 `<p>` 来标记段落。

font-size 值可以是绝对或相对值。

绝对值：

* 将文本设置为指定的大小
* 不允许用户在所有浏览器中改变文本大小（不利于可用性）
* 绝对大小在确定了输出的物理尺寸时很有用

相对大小：

* 相对于周围的元素来设置大小
* 允许用户在浏览器改变文本大小

使用像素来设置字体大小

通过像素设置文本大小，可以对文本大小进行完全控制：

    h1 {font-size:60px;}
    h2 {font-size:40px;}
    p {font-size:14px;}


使用 em 来设置字体大小

如果要避免在 Internet Explorer 中无法调整文本的问题，许多开发者使用 em 单位代替 pixels。

W3C 推荐使用 em 尺寸单位。

1em 等于当前的字体尺寸。如果一个元素的 font-size 为 16 像素，那么对于该元素，1em 就等于 16 像素。在设置字体大小时，em 的值会相对于父元素的字体大小改变。

浏览器中默认的文本大小是 16 像素。因此 1em 的默认尺寸是 16 像素。

可以使用下面这个公式将像素转换为 em：pixels/16=em

    h1 {font-size:3.75em;} /* 60px/16=3.75em */
    h2 {font-size:2.5em;}  /* 40px/16=2.5em */
    p {font-size:0.875em;} /* 14px/16=0.875em */


结合使用百分比和 EM


在所有浏览器中均有效的方案是为 body 元素（父元素）以百分比设置默认的 font-size 值：

    body {font-size:100%;}
    h1 {font-size:3.75em;}
    h2 {font-size:2.5em;}
    p {font-size:0.875em;}

### 4.CSS链接

基本上就是 `<a>` 标签。

链接的四种状态：

* a:link - 普通的、未被访问的链接
* a:visited - 用户已访问的链接
* a:hover - 鼠标指针位于链接的上方
* a:active - 链接被点击的时刻

可以分别为处于不同状态的链接，设置不同的样式。

    a:link {color:#FF0000;}		/* 未被访问的链接 */
    a:visited {color:#00FF00;}	/* 已被访问的链接 */
    a:hover {color:#FF00FF;}	/* 鼠标指针移动到链接上 */
    a:active {color:#0000FF;}	/* 正在被点击的链接 */

当为链接的不同状态设置样式时，请按照以下次序规则：

a:hover 必须位于 a:link 和 a:visited 之后

a:active 必须位于 a:hover 之后


#### (1)文本修饰

`text-decoration` 属性大多用于去掉链接中的下划线：

    a:link {text-decoration:none;}
    a:visited {text-decoration:none;}
    a:hover {text-decoration:underline;}
    a:active {text-decoration:underline;}


#### (2)背景色
background-color 属性规定链接的背景色：

    a:link {background-color:#B2FF99;}
    a:visited {background-color:#FFFF85;}
    a:hover {background-color:#FF704D;}
    a:active {background-color:#FF704D;}

### 5.CSS列表

从某种意义上讲，不是描述性的文本的任何内容都可以认为是列表。人口普查、太阳系、家谱、参观菜单，甚至你的所有朋友都可以表示为一个列表或者是列表的列表。


#### (1)列表类型
要影响列表的样式，最简单（同时支持最充分）的办法就是改变其标志类型。

例如，在一个无序列表中，列表项的标志 (marker)
是出现在各列表项旁边的圆点。在有序列表中，标志可能是字母、数字或另外某种计数体系中的一个符号。
要修改用于列表项的标志类型，可以使用属性 `list-style-type`：

    ul {list-style-type : square}

上面的声明把无序列表中的列表项标志设置为方块。

#### (2)列表项图像
有时，常规的标志是不够的。你可能想对各标志使用一个图像，这可以利用 `list-style-image` 属性做到：

    ul li {list-style-image : url(xxx.gif)}
    
只需要简单地使用一个 url() 值，就可以使用图像作为标志。

简写列表样式
为简单起见，可以将以上 3 个列表样式属性合并为一个方便的属性：`list-style`，就像这样：

    li {list-style : url(example.gif) square inside}
    
list-style 的值可以按任何顺序列出，而且这些值都可以忽略。只要提供了一个值，其它的就会填入其默认值。


### 6.CSS 表格

#### (1)表格边框

    table, th, td{
        border: 1px solid blue;
    }
为 table、th 以及 td 设置了蓝色边框

#### (2)表格宽度和高度
通过 `width` 和 `height` 属性定义表格的宽度和高度。
下面的例子将表格宽度设置为 100%，同时将 th 元素的高度设置为 50px：

    table {
        width:100%;
    }
    
    th {
        height:50px;
    }
    
#### (3)表格文本对齐
`text-align` 和 `vertical-align` 属性设置表格中文本的对齐方式。
text-align 属性设置水平对齐方式，比如左对齐、右对齐或者居中：

    td {
        text-align:right;
    }
    
vertical-align 属性设置垂直对齐方式，比如顶部对齐、底部对齐或居中对齐：

    td {
        height:50px;
        vertical-align:bottom;
    }
    
## 三 CSS 框模型

<div> 标签

![233](div.png)

设置 `margin` `padding` 两个主要属性和  `width` `height`。


#### 边框的宽度
您可以通过 border-width 属性为边框指定宽度。

所以，我们可以这样设置边框的宽度：

    p { 
        border-style: solid;
         border-width: 5px;
    }
    

## 四 CSS 定位

### **1.CSS 定位和浮动**

CSS 为定位和浮动提供了一些属性，利用这些属性，可以建立列式布局，将布局的一部分与另一部分重叠，还可以完成多年来通常需要使用多个表格才能完成的任务。

定位的基本思想很简单，它允许你定义元素框相对于其正常位置应该出现的位置，或者相对于父元素、另一个元素甚至浏览器窗口本身的位置。显然，这个功能非常强大，也很让人吃惊。要知道，用户代理对 CSS2 中定位的支持远胜于对其它方面的支持，对此不应感到奇怪。

另一方面，CSS1 中首次提出了浮动，它以 Netscape 在 Web 发展初期增加的一个功能为基础。浮动不完全是定位，不过，它当然也不是正常流布局。我们会在后面的章节中明确浮动的含义。


### **2.一切皆为框**

div、h1 或 p 元素常常被称为块级元素。这意味着这些元素显示为一块内容，即“块框”。与之相反，span 和 strong 等元素称为“行内元素”，这是因为它们的内容显示在行中，即“行内框”。

您可以使用 display 属性改变生成的框的类型。这意味着，通过将 display 属性设置为 block，可以让行内元素（比如 `<a>` 元素）表现得像块级元素一样。还可以通过把 display 设置为 none，让生成的元素根本没有框。这样的话，该框及其所有内容就不再显示，不占用文档中的空间。

但是在一种情况下，即使没有进行显式定义，也会创建块级元素。这种情况发生在把一些文本添加到一个块级元素（比如 div）的开头。即使没有把这些文本定义为段落，它也会被当作段落对待：

### **3.CSS 定位机制**

CSS 有三种基本的定位机制：
* 普通流
* 浮动
* 绝对定位。

除非专门指定，否则所有框都在普通流中定位。也就是说，普通流中的元素的位置由元素在 (X)HTML 中的位置决定。

块级框从上到下一个接一个地排列，框之间的垂直距离是由框的垂直外边距计算出来。

行内框在一行中水平布置。可以使用水平内边距、边框和外边距调整它们的间距。但是，垂直内边距、边框和外边距不影响行内框的高度。由一行形成的水平框称为行框（Line Box），行框的高度总是足以容纳它包含的所有行内框。不过，设置行高可以增加这个框的高度。



### (1) CSS 相对定位

相对定位是一个非常容易掌握的概念。如果对一个元素进行相对定位，它将出现在它所在的位置上。然后，可以通过设置垂直或水平位置，让这个元素“相对于”它的起点进行移动。

如果将 top 设置为 20px，那么框将在原位置顶部下面 20 像素的地方。如果 left 设置为 30 像素，那么会在元素左边创建 30 像素的空间，也就是将元素向右移动。

    #box_relative {
        position: relative;
        left: 30px;
        top: 20px;
    }


### (2) CSS 绝对定位

CSS `position` 属性

通过使用 position 属性，我们可以选择 4 种不同类型的定位，这会影响元素框生成的方式。

* static
元素框正常生成。块级元素生成一个矩形框，作为文档流的一部分，行内元素则会创建一个或多个行框，置于其父元素中。

* relative
元素框偏移某个距离。元素仍保持其未定位前的形状，它原本所占的空间仍保留。

* absolute
元素框从文档流完全删除，并相对于其包含块定位。包含块可能是文档中的另一个元素或者是初始包含块。元素原先在正常文档流中所占的空间会关闭，就好像元素原来不存在一样。元素定位后生成一个块级框，而不论原来它在正常流中生成何种类型的框。

* fixed
元素框的表现类似于将 position 设置为 absolute，不过其包含块是视窗本身。
提示：相对定位实际上被看作普通流定位模型的一部分，因为元素的位置相对于它在普通流中的位置。



























