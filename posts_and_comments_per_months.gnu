
set xdata time
set timefmt "%Y-%m-%d"
set format x "%m/%y"

INCR=20
set key inside top right

set ytics nomirror
set y2tics 
set link y2 via y/INCR inverse y*INCR

set title "Статистика сообщества ру-чп\nЧисло комментариев"
set xlabel 'Месяцы'
set y2label 'Количество постов'
set ylabel 'Количество комментариев'


plot  "comments_posts_monthly.txt" using 1:2 title 'Комментарии' with lines, "comments_posts_monthly.txt" using 1:(INCR*$3) title 'Посты' with lines

pause -1