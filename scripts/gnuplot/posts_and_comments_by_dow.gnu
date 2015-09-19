set terminal png size 500,400 
set output 'posts_comments_by_dow.png'

set datafile separator ","

#set key inside top right

#set linestyle 1 lt 1 lw 50

set title "Статистика сообщества #####\nКоличество постов по дням недели"
#set title "Статистика сообщества ру-чп\nКоличество постов по дням недели"
set xlabel 'День недели'
set ylabel 'Количество постов'


plot  "results/comments_posts_by_dow.csv" every ::1 using 1:4:xtic(2) title '' with boxes fs solid

#pause -1