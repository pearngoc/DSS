# slide_VS (1)

Source: `slide_VS (1).pdf`  
Slides: 77

## Slide 1

Data Visualization

> This slide also contains a figure that is not represented as text.

## Slide 2 — Introduction of Visualization

“The use of computer-supported, interactive, visual representations of abstract data to amplify cognition”

Card, Mackinlay, & Shneiderman

- Computer-supported: Not hand-drawn.
- Interactive: Zoom, filter, hover.
- Abstract Data: Stocks, Votes, Sales (Non-physical data)
- Amplify Cognition: Make you smarter.

## Slide 3

Introduction of Visualization

Raw Data

Heatmap

> This slide also contains a figure that is not represented as text.

## Slide 4 — Introduction of Visualization

> This slide is mostly a figure. Only the title text could be extracted.

## Slide 5 — Data Abstraction

Data visualization

Chapter 4

> This slide also contains a figure that is not represented as text.

## Slide 6 — Data abstraction

- Data level
  - There are five basic data types
    - Attribute– property that can be measured

 Salary, price, temperature,…

    - Item– individual entity

 A row of a table, a node in a network…

    - Link – relationship between items
    - Position – spatial/ location

 Latitude–longitude,

    - Grid – how to samples continuous data

 Geometric, topological

  - Data semantics
- Dataset level
  - There are four basic types
    - Tables
    - Networks
    - Fields
    - Geometry

## Slide 7 — Data level: Items & Attributes

- item: individual entity, discrete
  - eg patient, car, stock, city
  - "independent variable"

item: person

## Slide 8 — Data level: Items & Attributes

- item: individual entity, discrete
  - eg patient, car, stock, city
  - "independent variable"
- attribute: property that is measured, observed, logged...
  - eg height, blood pressure for patient
  - "dependent variable"

item: person

## Slide 9 — Dataset level

- flat table
  - one item per row
  - each column is attribute
  - cell holds value for item-attribute pair

attributes: name, age, shirt size, fave fruit

item: person

## Slide 10 — Dataset level

- flat table
  - one item per row
  - each column is attribute
  - cell holds value for item-attribute pair
  - unique key (could be implicit) attributes: name, age, shirt size, fave fruit

item: person

## Slide 11 — Dataset level

- multidimensional tables
  - indexing based on multiple keys
    - eg genes, patients

## Slide 12 — Dataset level

- The 3D table uses three indices to find a cell
> This slide also contains a figure that is not represented as text.

## Slide 13 — Dataset availability

- There are two kinds of dataset availability: static and dynamic
- Static file means the entire dataset is available all at once
- Dynamic streams mean a dataset is continuously generated, by different sources, without having access to all the data

## Slide 14 — Attribute types: categorical vs ordered

- Categorical (nominal)
  - Equal or not equal to other values
  - Ex: gender, student number, course name,…
  - No concept of relative relation other than inclusion in the set
- Ordered
  - Implicit ordering
  - There are two ordered types: ordinal and quantitative
    - Ordinal – well-defined ordering but without full-fledged arithmetic
    - Quantitative – well-defined capability to perform arithmetic and comparison

## Slide 15 — Ordered attribute type: direction

- An ordered dataset can be sequential or diverging.
  - A sequential dataset has a homogeneous range from a minimum to a maximum.
  - A diverging dataset has data measured from a based point and extends to both ends
  - A cyclic dataset has its values wrapped around back to a starting point

## Slide 16 — Attributes: hierarchical

- An attribute may have a hierarchical structure.
- Ex:
  - Date sold products: 15/10/2022 (weeks, months, years)
  - A geographic attribute of a postal code may be aggregated to the level of cities, states,…

Cần Thơ Ninh Kiều An Hòa

Province/ City district/ town ward

## Slide 17 — Attribute types: categorical vs ordered

- Continuous
  - Data can take any value within the range
  - Ex: Number grade
- Discrete
  - Data can take only certain values
  - Ex: Letter grade (A+)
- We can convert between these using clustering or thresholds

## Slide 18 — Data semantics

- Definition

Semantics = Real-world meaning attached to data (Metadata).

- The "Basil 7 S Pear" Puzzle:
  - Data: string "Basil 7 S Pear".
  - Hypothesis:
    - Sales: A food shipment (Basil + Pears) arriving on the 7th?
    - Services: "Basil Point" neighborhood has 7 inches of snow, cleared by "Pear Creek" company?
    - Experiment: A lab rat named "Basil" took 7 tries to run the

"South" maze for a "Pear" reward?

 Visualization requires understanding semantics to choose the right display.

## Slide 19 — Data semantics – Key and Value

- Key semantics
  - A key attribute is an index that is used to find value attributes
  - In a table, the key may just be explicit or implicit (indices)
  - Keys may be categorical or ordinal attributes
- Value attribute is a value of the table cell

## Slide 20 — l

> This slide is mostly a figure. Only the title text could be extracted.

## Slide 21 — How to Design Vis. Idioms?

Idiom

What

How

Why

Chart name

Data abstraction

Encoding

Manipulate

Facet

Reduce

Task abstraction

## Slide 22 — Mark & Channel

Data visualization

Chapter 4

> This slide also contains a figure that is not represented as text.

## Slide 23 — Marks as items/nodes

- A mark is a basic graphical element in an image.
- Marks are geometric primitives classified according to the number of dimensions they require
- Points – 0D Lines – 1D Areas – 2D Volume – 3D

## Slide 24 — Channels

- A visual channel is a way to control the appearance of the mark, independent of the dimensionality of the geometric primitives
- Commonly seen channel types: position, color, shape, tilt,and size
- Other possible channels: depth, luminance, saturation, curvature, …

## Slide 25 — Channels

> This slide is mostly a figure. Only the title text could be extracted.

## Slide 26 — Visual encoding

Item  Mark

A ttr ib u te



Ch an n el

> This slide also contains a figure that is not represented as text.

## Slide 27 — Visualization building blocks

Mark

Channel

Num of attributes encoded: 2

> This slide also contains a figure that is not represented as text.

## Slide 28 — Visualization building blocks

Mark

Channel

Num of attributes encoded: 2

> This slide also contains a figure that is not represented as text.

## Slide 29 — Visualization building blocks

Mark

Channel

Num of attributes encoded: 3

> This slide also contains a figure that is not represented as text.

## Slide 30 — Visualization building blocks

Mark

Channel

Num of attributes encoded: 4

> This slide also contains a figure that is not represented as text.

## Slide 31 — Visualization building blocks

Mark

Channel

Num of attributes encoded: 2

> This slide also contains a figure that is not represented as text.

## Slide 32 — Visualization building blocks

Mark

Channel

Num of attributes encoded: 2

> This slide also contains a figure that is not represented as text.

## Slide 33 — Visualization building blocks

Mark

Channel

Num of attributes encoded: 3

> This slide also contains a figure that is not represented as text.

## Slide 34 — Color

Data visualization

Chapter 4

> This slide also contains a figure that is not represented as text.

## Slide 35 — Big picture

> This slide is mostly a figure. Only the title text could be extracted.

## Slide 36 — Color spaces

- The color space of what colors the human visual system can detect is three-dimensional
- Some of these color spaces are for computer manipulation, and the others are a better match with the characteristic of human vision
- The most common color space is the RGB system
  - Each color is represented by the weights assigned to the red, green and blue channels.

## Slide 37 — Color spaces

- HSL system
  - Requires HUE, Saturation, and Lightness axis
  - Each color is defined by the weights assigned to the

HUE, saturation and lightness axis

    - HUE axis captures what we normally think of as pure color

Not mixed with pure white and pure black

    - Saturation axis is the amount of white mixed with a pure color

Pink = red + pure white

    - Lightness axis is the amount of black mixed with a color
- HSV space is similar, where V is for grayscale and is linear to lightness L

## Slide 38 — Luminance, Saturation and HUE Channels

- Luminance, saturation and HUE can be used as a magnitude channel and as an identity channel
  - Magnitude channel
    - Luminance
    - Saturation
  - Identify channel
    - HUE

## Slide 39 — Luminance, Saturation and HUE Channels

- Magnitude channel
  - Luminance

Suitable for ordered data

Low-accuracy channel in terms of perceiving whether noncontiguous regions have the same luminance because of contrast effects

Limit grayscale bins to no more than 4

  - Saturation
- Identify channel
  - HUE

## Slide 40 — Luminance, Saturation and HUE Channels

- Magnitude channel
  - Luminance
  - Saturation

Suitable for ordered data

Low-accuracy for noncontiguous regions

The number of discriminate steps for saturation is low: around 3 bins

Interact with the size channel

Use bright, highly saturated colors so that small regions are more distinguishable

- Identify channel
  - HUE

## Slide 41 — Luminance, Saturation and HUE Channels

- Identify channel
  - HUE

Very effective for categorical data and showing groups (highest ranked after spatial position)

HUE and size can interact: HUE is harder to distinguish in small regions

Make fine distinctions in HUE for contiguous regions

Very limited discriminability between separate regions

HUE does not have an implicit perceptual ordering

## Slide 42

Colormaps

> This slide is mostly a figure. Only the title text could be extracted.

## Slide 43 — Colormaps

- A colormap defines a mapping between colors and data values (visual encoding with colors)
- Colormaps can be categorical or ordered
  - Ordered colormaps can be sequential or diverging
- Colormaps can also be a continuous range of values or segmented into discrete bins of colors
  - Continuous colormaps are used for showing quantitative attributes
  - Segmented colormaps are suitable for categorical data
  - For ordinal data
    - Segmented colormaps will emphasize their discrete nature
    - While continuous colormaps will emphasize their ordered nature

## Slide 44 — Colormaps

> This slide is mostly a figure. Only the title text could be extracted.

## Slide 45 — Categorical Colormaps

- For other uses, colors should be sufficiently different in luminance that they can be distinguished even in black and white
- Colormaps for
  - Small regions such as lines should be highly saturated
  - Large regions such as areas should have low saturation
- An appropriate colormap may depend on the mark type being used.

## Slide 46 — Categorical Colormaps - Example

ColorBrewer: Color Advice for Maps

> This slide also contains a figure that is not represented as text.

## Slide 47 — Categorical Colormaps - Example

> This slide is mostly a figure. Only the title text could be extracted.

## Slide 48 — Categorical Colormaps - Example

> This slide is mostly a figure. Only the title text could be extracted.

## Slide 49 — Ordered Colormaps

- An ordered colormap is appropriate for encoding ordinal or quantitative attributes
- The two major variants of continuous colormaps for ordered data have expressiveness characteristics that should match up with the attribute type.
  - Sequential
  - Diverging

## Slide 50 — Ordered Colormaps

- A sequential colormap
  - Ranges from a minimum value to a maximum value
  - If only the luminance channel is used, the result is a grayscale ramp
    - When hue is added, one end of the map is a specific hue at full saturation and brightness
  - If saturation is a variable, the other end is pale or white
    - If luminance is the varying quantity, the other end is dark or black
- A diverging colormap
  - has two hues at the endpoints and a neutral color as a midpoint
  - This neutral color may be white, gray, or black, or a high- luminance color such as yellow.

## Slide 51 — Colorblind-Safe Colormaps

- Color blindness is a sex-linked inherited trait that affects 8% of males and 0.5% of females.
  - In the common forms of color blindness, the ability to sense along the red-green color axis is limited or absent.
  - Many pairs that are discriminable to people with normal color vision are confused
    - Including red-black, blue-purple, light green-white, and brown-green.

## Slide 52 — Colorblind-Safe Colormaps

- Avoid the use of only the HUE channel to encode information
  - In addition to HUE design, categorical colormaps vary in luminance or saturation
- If possible, avoid colormaps that emphasize red- green
  - Especially in divergent red-green ramps

## Slide 53

Expressiveness & Effectiveness principles

> This slide also contains a figure that is not represented as text.

## Slide 54 — Expressiveness

> This slide is mostly a figure. Only the title text could be extracted.

## Slide 55 — Effectiveness

- The effectiveness principle states that
  - The importance of the attribute
    - Match the salience of the channel
    - Encoded with the most effective channels in order to be most noticeable
  - Less important attributes
    - Matched with less effective channel

## Slide 56 — Effectiveness

- Spatial channels are the only ones that appear on both lists at the top
- None of the others are effective for both data types
- The above channels are for

2D, and 3D depth is a much lower channel

## Slide 57 — Channel effectiveness

- How do we identify the effectiveness of a channel?
  - The criteria of effectiveness channel
    - Accuracy
      - How precisely can we tell the difference between encoded items?
    - Discriminability
      - How many unique steps can we perceive?
    - Separability
      - Is our ability to use this channel affected by another one?
    - The ability to provide visual popout
      - Can things jump out using this channel?
    - The ability to provide perceptual grouping

## Slide 58 — Accuracy

Results largely confirmed Cleveland & McGill (1984) with respect to the relative order.

The area judgment tasks are shown to give even larger errors T

1

<

T

2

<

T

3

<

T

4

<

T

5

<

T

6

<

T

8

<

T

9

<

T

7

## Slide 59 — Discriminability

- Discriminability
  - If a data attribute is encoded using a particular visual channel, are the differences between items (of this attribute) perceptible to the human as intended?
  - The characterization of a visual channel should quantify the number of bins that are available for use within a visual channel, where each bin is a distinguishable step
- EX:
  - Changing line width past a certain limit may be perceived as an area rather than a line mark
- Line width may be very usable for a small number of different values
  - But would be a poor choice for dozens or hundreds of values

## Slide 60 — Discriminability

> This slide is mostly a figure. Only the title text could be extracted.

## Slide 61 — Discriminability

100 +

10+

4 - 6

4 - 6

2 - 3

3 - 7

3 - 5

2 - 4

2 - 4

2 – 10+

6 - 12

2 - 4

5 - 8

## Slide 62 — Separability

- Visual channels are not completely independent of each other
  - Because some have dependencies and interactions with others.
- Consider potential interaction between visual channels
  - Ranging from the orthogonal and independent separable channels to the inextricably combined integral channels.
- Visual encoding separable channels is straightforward
  - But encoding different information in integral channels will fail

## Slide 63 — Separability

> This slide is mostly a figure. Only the title text could be extracted.

## Slide 64 — Visual Popout

- Visual Popout: Making a distinct item stands out from many others immediately.
- Popout is also known as pre-attentive processing or tunable detection.
- Our low-level visual system can help spot in parallel the different objects from many distracting objects, without the need for the viewer to consciously direct attention to the item one by one.
- In fact, this capability is independent of the number of distracting items.

## Slide 65 — Visual Popout

The red circle pops out from a small set of blue circles.

We recognize this instantly

## Slide 66 — Visual Popout

The red circle pops out from a few squares

It is a bit slower than with color, though.

## Slide 67 — Visual Popout

The red circle also pops out from a small set of mixed shapes and colors.

> This slide also contains a figure that is not represented as text.

## Slide 68 — Visual Popout

Tilt Size Shape

Proximity Shadow Direction Tilted line pairs

Many channels support visual popout

## Slide 69 — Ví dụ

- “Quản lý muốn biết thể loại sách nào đang mang lại doanh thu cao nhất và mối tương quan giữa giá sách và số lượng bán ra của từng cuốn sách để quyết định chương trình khuyến mãi tiếp theo."
- Bảng dữ liệu gồm:
  - Mã_sách
  - Tên_sách
  - Thể_loại (Văn học, Khoa học, Thiếu nhi)
  - Giá_tiền (VNĐ)
  - Số_lượng_bán (cuốn)
  - Doanh_thu (VNĐ).

## Slide 70 — Data abstraction

- Data type: item/attribute
- Dataset type: table
- Dataset availability: static
- Item semantic: mỗi dòng là một cuốn sách cụ thể

Attribute Type Key/ Direction Hierarchical Continuous Semantic

Name (C,O,Q) value

Thể loại C Val

Giá tiền Q Val Tuần tự

Số lượng Q Val Tuần tự bán

Doanh thu Q Val Tuần tự

/ Discrete

Rời rac

Liên tục

Rời rạc

Liên tục

Tên thể loại

Giá bán sp

Số lượng bán sp

Doanh thu

## Slide 71 — Task abstraction

- Task_1:Tìm thể loại sách mang lại doanh thu cao nhất

 So sánh + giá trị lớn nhất

- Task_2:Tìm mối tương quan giữa giá sách và số lượng bán ra của từng cuốn

=> Tương quan + 2 thuộc tính (giá vs số lượng)

## Slide 72 — Idioms

Idiom Bar chart

What

How

Why

- Thể loại (1)

- Tổng doanh thu (1)

Encoding

Mark: line

Channel

- Pos x: tổng doanh thu

- Region y: thể loại

- Color: thể loại

Compare + extreme

## Slide 73 — Vẽ biểu đồ

> This slide is mostly a figure. Only the title text could be extracted.

## Slide 74 — Đánh giá kỹ thuật

Biểu đạt; C  region; Q  position

Hiệu quả:

1. Độ chính xác (Accuracy): T1

2. Khả năng phân biệt (Discriminability):

- 3 region (10+)
- 3 color (6-12)
- pos y (100+)

3. Khả năng phân tách (Separability):

- Vị trí + màu sắc  phân tách
- Vị trí dọc + vị tri ngang  phân tách

4. Khả năng nổi bật thị giác (Visual Popout)

5. Khả năng gom nhóm nhận thức (Perceptual

Grouping)

## Slide 75 — Đánh giá nhận thức

Task_1:Tìm thể loại sách mang lại doanh thu cao nhất

Thể loại thiếu nhi dẫn đầu doanh thu vượt trội với 519.0 triệu VNĐ (chiếm khoảng 47% tổng doanh thu), vượt xa hai thể loại còn lại.

## Slide 76 — Thiết kế dashboard và đánh giá

1. Phân tích nhiệt độ theo không gian & địa hình

- So sánh nhiệt độ trung bình giữa các vùng trên toàn quốc
- So sánh nhiệt độ trung bình/cao nhất/thấp nhất giữa các loại địa hình.
- So sánh tỉnh ven biển & nội địa.
- Thống kê mật độ điểm đo phân bố theo từng khu vực.

2. Phân tích biến động theo thời gian & thời tiết

- Xu hướng biến động nhiệt độ theo mùa
- Tần suất xuất hiện của các trạng thái thời tiết và nhiệt độ theo trạng thái thời tiết.
- So sánh thời tiết giữa các vùng.

3. Phân tích bức xạ mặt trời & thiên văn

- Tương quan giữa chỉ số UV và nhiệt độ.
- Tương quan giữa độ dài ban ngày và chỉ số UC trung bình theo từng tháng trong năm.

## Slide 77

Q & A

> This slide is mostly a figure. Only the title text could be extracted.
