
# CSS

## 选择器

选择器是一种可以帮助你**快速定位元素**的工具，定位之后可以对这些元素进行样式的设定

### 1.基本选择器
    .selector {
        property: value
    }


    h1 {color:red; font-size:14px;}

### 2.派生选择器
    li strong {
        font-style: italic;
        font-weight: normal;
    }
    
li 中的 strong 标签

    <p><strong>我是粗体字，不是斜体字，因为我不在列表当中，所以这个规则对我不起作用</strong></p>
    
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

    #red p{
    }

基于id的 派生选择器


### 4. 类选择器

    .center {
        text-align: center;
    }


    <h1 class="center">
    This heading will be center-aligned
    </h1>

    <p class="center">
    This paragraph will also be center-aligned.


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

    p {
        background-color: gray;
    }

如果您希望背景色从元素中的文本向外少有延伸，只需增加一些内边距：

    p {
        background-color: gray;
        padding: 20px;
    }

`background-color` 不能继承，其默认值是 `transparent`。`transparent` 有“透明”之意。也就是说，如果一个元素没有指定背景色，那么背景就是透明的，这样其祖先元素的背景才能可见。

#### (2)背景图像

    body {
        background-image: url(/i/eg_bg_04.gif);
    }

如果需要在页面上对背景图像进行平铺，可以使用 `background-repeat` 属性。

    body
    { 
      background-image: url(/i/eg_bg_03.gif);
      background-repeat: repeat-y;
    }

可以利用 `background-position` 属性改变图像在背景中的位置。
在 `body` 元素中将一个背景图像居中放置：

    body
    { 
        background-image:url('/i/eg_bg_03.gif');
        background-repeat:no-repeat;
        background-position:center;
    }

#### 背景关联
如果文档比较长，那么当文档向下滚动时，背景图像也会随之滚动。当文档滚动到超过图像的位置时，图像就会消失。
您可以通过 `background-attachment` 属性防止这种滚动。通过这个属性，可以声明图像相对于可视区是固定的（fixed），因此不会受到滚动的影响：

    body 
    {
        background-image:url(/i/eg_bg_02.gif);
        background-repeat:no-repeat;
        background-attachment:fixed
    }

  
### 2.文本

#### (1)缩进文本
把 Web 页面上的段落的第一行缩进，这是一种最常用的文本格式化效果。
CSS 提供了 `text-indent` 属性，该属性可以方便地实现文本缩进。
通过使用 `text-indent` 属性，所有元素的第一行都可以缩进一个给定的长度，甚至该长度可以是负值。
这个属性最常见的用途是将段落的首行缩进，下面的规则会使所有段落的首行缩进` 5 em`：

    p {
        text-indent: 5em;
    }







