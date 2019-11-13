# R has a wide variety of data tyoes including:
# scalars, vectors (numerical, character, logical), matrices, dataframes, and lists

# Scalars: THe most basic way to store a number is through assignemnt
# Assignment operator is <-
a <- 9
a
a + 5

b <- sqrt(a)
b

#Nonscalar data types:
# Easiest way to store list of numbers, through assignmnet, using c() -- combine function
# Vectors (one-dimensional arrays), by default, are specified with the c() function
g <- c(1,2,3,4,5,6,7-2,4)
# or c <- vector(1,2,3,4,5,6,7,-2,4) # also works
g
typeof(g) #print datatype
is.list(g) #False
is.vector(g) #True

d<-c("one", "two", "three") #character vector
d
typeof(d)

e<-c(TRUE,TRUE,TRUE,FALSE,TRUE,FALSE) #logical vector
e
typeof(e)

#To refer to a row in Python use index
#In R, refer to object in ith row and jth column by OBJECTNAME[i,j]
#In R, refer to column name with OBJEECTNAME$Columname
#R index starts at 1
d[1]

#string is specified by using quotes, single or double
my_str<- 'Hello World!'
my_str
typeof(my_str)

#Some instrinsic functions on vector a and vector c
sqrt(a)

sqrt(g) #No error, it did not calculate the negative number

a^2 #square a scalar
g^2 # squares every number in the vector

min(g)
max(g)
mean(g)
sum(g)

#read csv file
#read.csv() reads file into dataframe similar to python
#Requires one argument -- name of file
#can have three args
#  1. Name of file
#  2. Indicates if first row in data or header head=TRUE
#  3. sep indicates seperator sep=","
tech = read.csv("~/RProjects/TechCrunchcontinentalUSA.csv", header = TRUE, stringsAsFactors = FALSE)
tech #display all data inside console
summary(tech) #prints info about each colum
head(tech)        #Functions for getting info
tail(tech)
colnames(tech)

dir() #shows files/subdirs in current directory
getwd() #shows path of current directory

names(tech) #same a colnames
tech$company
attributes(tech)

ls() #prints list of variables used in session
     # just look in top left corner

#Basic statistics
mean(tech$raisedAmt)

#Fix: remove missing values
# will not return result if any values missing unless specify na.rm=TRUE
var(tech$raisedAmt)
sd(tech$raisedAmt)
quantile(tech$raisedAmt)

#complete.cases() returns vector indicating which cases are complete
#list rows of data with missing values
tech[!complete.cases(tech),]

#na.omit() returns logical vector indiicating which cases are complete
# create new dataset without missing values
tech_no_missing_data <- na.omit(tech)
tech_no_missing_data

#Charting/Plotting
help("stripchart")
stripchart(tech_no_missing_data$raisedAmt) #strip chart

#histogram
hist(tech$numEmps, breaks = 2, main="Amount each company has raised", xlab = "Amount of $")

#boxplot
boxplot(tech$numEmps)
# or plotted horizontally
boxplot(tech$numEmps, main='something', xlab='companies', horizontal = TRUE)

#scatter plot provides graphical view of relationship between two sets of numbers
plot(tech$numEmps, tech$raisedAmt, main='Relationship', xlab = "num", ylab = "amount")



