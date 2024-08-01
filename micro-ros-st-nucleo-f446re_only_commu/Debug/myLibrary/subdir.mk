################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (11.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../myLibrary/AK_60_task.c \
../myLibrary/communication.c \
../myLibrary/controller.c \
../myLibrary/motor_config.c 

C_DEPS += \
./myLibrary/AK_60_task.d \
./myLibrary/communication.d \
./myLibrary/controller.d \
./myLibrary/motor_config.d 

OBJS += \
./myLibrary/AK_60_task.o \
./myLibrary/communication.o \
./myLibrary/controller.o \
./myLibrary/motor_config.o 


# Each subdirectory must supply rules for building sources it contributes
myLibrary/%.o myLibrary/%.su myLibrary/%.cyclo: ../myLibrary/%.c myLibrary/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F446xx -c -I../Core/Inc -I"/home/ros2/STM32CubeIDE/workspace_1.13.2/micro-ros-st-nucleo-f446re_only_commu/myLibrary" -I../micro_ros_stm32cubemx_utils/microros_static_library_ide/libmicroros/include -I../Drivers/STM32F4xx_HAL_Driver/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F4xx/Include -I../Drivers/CMSIS/Include -I../Middlewares/Third_Party/FreeRTOS/Source/include -I../Middlewares/Third_Party/FreeRTOS/Source/CMSIS_RTOS_V2 -I../Middlewares/Third_Party/FreeRTOS/Source/portable/GCC/ARM_CM4F -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-myLibrary

clean-myLibrary:
	-$(RM) ./myLibrary/AK_60_task.cyclo ./myLibrary/AK_60_task.d ./myLibrary/AK_60_task.o ./myLibrary/AK_60_task.su ./myLibrary/communication.cyclo ./myLibrary/communication.d ./myLibrary/communication.o ./myLibrary/communication.su ./myLibrary/controller.cyclo ./myLibrary/controller.d ./myLibrary/controller.o ./myLibrary/controller.su ./myLibrary/motor_config.cyclo ./myLibrary/motor_config.d ./myLibrary/motor_config.o ./myLibrary/motor_config.su

.PHONY: clean-myLibrary

