setwd("Users/spencerfinkel/repos/lis4369/p2")
# using their data set...same dataset
data("mtcars")
View(mtcars)
#view data by explicitly writing the variable name
mtcars

# remember indexing starts at 1
head(mtcars, 10)

tail(mtcars, 10)

summary(mtcars)
names(mtcars)
data.frame(mtcars)   ##all of this does the same thing...display data
structure(mtcars)
attributes(mtcars)

colnames(mtcars)  # display column names

mtcars[1,] # dsiplays first row with colnames

mtcars[,1]

mtcars$cyl # display column data using name

mtcars[3,3]

mtcars[mtcars$cyl > 4,] # use index notation to return certain info

mtcars[mtcars$cyl > 4 & mtcars$gear >= 5,] # use and operator to combine conditions

mtcars[mtcars$cyl > 4 & mtcars$gear == 4,]

mtcars[mtcars$cyl > 4 | mtcars$gear == 4,]

mtcars[mtcars$cyl > 4 & mtcars$gear != 4,]

nrow(mtcars) # number of rows

ncol(mtcars)    
length(mtcars)  # these are same

dim(mtcars) # rows and columns   out: 32 11

data.frame(mtcars)

str(mtcars)   #this shows structure... not string

summary(mtcars$hp)

library('psych')

describe(mtcars$hp)  #this shows all
mean(mtcars$hp)           #
median(mtcars$hp)         #
min(mtcars$hp)            #
max(mtcars$hp)            #
quantile(mtcars$hp)       #
var(mtcars$hp)            #
sd(mtcars$hp)             #

library('ggplot2')
qplot(mpg, hp, data=mtcars, color = factor(cyl), geom=c("point", "smooth"))             
counts <- table(mtcars$cyl, mtcars$mpg)
barplot(counts, main='Car distribution by Cylinder Amount and MPG', xlab = 'VS',legend = rownames(counts), beside=TRUE)

