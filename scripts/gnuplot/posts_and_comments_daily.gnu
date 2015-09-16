set terminal png size 3000,1000 
set output 'posts_comments_daily.png'

set datafile separator ","

set xdata time
set timefmt "%Y-%m-%d"
set format x "%m/%y"

INCR=20
INCR2=20
set key inside top right

set ytics nomirror
set y2tics 
set link y2 via y/INCR inverse y*INCR

set title "Статистика сообщества ру-чп\nЧисло комментариев в день"
#set xlabel 'Время'
set y2label 'Количество постов'
set ylabel 'Количество комментариев'


plot  "results/comments_posts_daily.csv" every ::1 using 1:2 title 'Комментарии' with lines,\
 "results/comments_posts_daily.csv" every ::1 using 1:(INCR*$3) title 'Посты' with lines,\
 "results/comments_posts_daily.csv" every ::1 using 1:(INCR2*$4) title 'Среднее количество комментариев/пост' with lines

#pause -1