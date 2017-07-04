# Tutorial by Data Science Dojo from https://www.youtube.com/watch?v=4vuw0AsHeGw
# practiced by Kin

# install.packages(c('ggplot2', # visualization 
#                    'e1071', # caret's dependency
#                    'caret', # 
#                    'quanteda', 
#                    'irlba', # SVD
#                    'randomForest'))

# load csv

spam.raw <- read.csv('spam.csv', stringsAsFactors = FALSE, fileEncoding="UTF-16")  # don't make it as Factors
# view(spam.raw)

# get 1st and 2nd columns only
spam.raw <- spam.raw[,1:2]
names(spam.raw) <- c('Label', 'Text')
head(spam.raw)

# check data to see any NA
length(which(!complete.cases(spam.raw))) 

# Convert the class lable into a factor
spam.raw$Label <- as.factor(spam.raw$Label)

# Investigate the data
# (1) See the Label's distribution
prop.table(table(spam.raw$Label))  # see the distribution by prop.table()

# (2) See the text's length distribution
spam.raw$TextLength <- nchar(spam.raw$Text)
summary(spam.raw$TextLength)

library(ggplot2)

ggplot(spam.raw, aes(x = TextLength, fill = Label)) +
  theme_bw() +
  geom_histogram(binwidth = 5) +
  labs(y = 'Text Count', x = 'Length of Text',
       title = 'Fistribution of the Text Length with Labels')
