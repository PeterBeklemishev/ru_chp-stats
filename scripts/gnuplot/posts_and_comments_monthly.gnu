set terminal png size 800,400 
set output 'posts_comments_monthly.png'

set datafile separator ","

set xdata time
set timefmt "%Y-%m-%d"
set format x "%m/%y"

INCR=20
set key inside top right

set ytics nomirror
set y2tics 
set link y2 via y/INCR inverse y*INCR

set title "Статистика сообщества ру-чп\nЧисло комментариев по месяцам"
set xlabel 'Месяцы'
set y2label 'Количество постов'
set ylabel 'Количество комментариев'


plot  "results/comments_posts_monthly.csv" every ::1 using 1:2 title 'Комментарии' with lines,\
 "results/comments_posts_monthly.csv" every ::1 using 1:(INCR*$3) title 'Посты' with lines

#pause -1