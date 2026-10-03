library(caret)

files <- list.files("data", pattern = "*.csv", full.names = TRUE)

results <- data.frame( )

for (file in files) {

    data <- read.csv(file)

    start_time <- Sys.time( )

    data[, ncol(data)] <- as.factor(data[, ncol(data)]) 

train_index <- createDataPartition(
  data[, ncol(data)],
  p = 0.8, 
  list = FALSE
)

train_data <- data[train_index, ]
test_data <- data[-train_index, ]

model <- glm(
     train_data[, ncol(train_data)] ~ . ,
     data = train_data,
     family = "binomial"
)


predictions <- predict(
    model, 
    test_data,
    type = "response"
)

predicted_class <- ifelse(predictions > 0.5, "1", "0")

actual <- test_data[, ncol(test_data)]

accuracy <- mean(predicted_class == actual)

print(file)

print(accuracy)

end_time <- Sys.time( )

execution_time <- end_time - start_time

execution_seconds <- as.numeric(execution_time)

power_watts <- 15

energy_wh <- power_watts * (execution_seconds / 3600)

co2_eq <- energy_wh * 0.475

print(execution_time)

print(energy_wh)

print(co2_eq)
}
