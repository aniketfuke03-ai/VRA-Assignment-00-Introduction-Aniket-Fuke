# Assignment 00 — Student Answer Sheet

## Student Information

| Field | Student Response |
|---|---|
| Full name | `[Aniket Pralhadrao Fuke]` |
| GitHub username | `[aniketfuke03-ai]` |
| Class/college | `[shankarlal khandelwal college (BAC-3rd year)]` |
| Submission date | `[10 Aug]` |

---

## Section A — Industrial Automation Fundamentals (15 marks)

### Q1. What is industrial automation? Explain it in 3–5 sentences. (5 marks)

`[Industrial automation means using machines and control systems to do industrial work automatically. It reduces human effort and saves time. It improves speed, accuracy, and safety. Examples are PLC, SCADA, sensors, and robots.]`

### Q2. State any four reasons industries use automation. (4 marks)

1. `[save time]`
2. `[reduce human effort]`
3. `[increase production]`
4. `[improve safety and accuracy]`

### Q3. Give three examples of processes that can be automated using PLC and SCADA. (3 marks)

1. `[Water treatment process]`
2. `[Power plant process]`
3. `[Factory production proces]`

### Q4. Complete the automation sequence. (3 marks)

```text
Input  →  Processing  →  Control  →  Output
```

Explain the meaning of each stage:

`[Input: Sensors collect information from the machine or environment, such as temperature, pressure, or level.]`

`[Processing: The PLC receives and checks the input data according to the programmed logic.]`

`[Control: The PLC sends a control signal to the required device.]`
`[Output: The device performs the required action, such as starting a motor or opening a valve.]`

---

## Section B — PLC Fundamentals and Working (25 marks)

### Q5. Expand PLC and explain why it is called an industrial computer. (5 marks)

`[PLC stands for Programmable Logic Controller.
It is called an industrial computer because it controls machines and industrial processes. It can take input from sensors, process the data, and control output devices. PLCs are strong, reliable, and designed to work in industrial environments.]`

### Q6. Classify each device as a PLC input or PLC output. (5 marks)

| Device | Input or Output? |
|---|---|
| Push button | `[Input]` |
| Proximity sensor | `[Input]` |
| Motor contactor | `[Output]` |
| Indicator lamp | `[Output]` |
| Temperature sensor | `[Input]` |

### Q7. Write the three main PLC working steps in the correct order. (6 marks)

1. `[Input Scan – PLC reads data from input devices like sensors and switches.]`
2. `[Program Scan – PLC processes the input data according to the stored program.]`
3. `[Output Scan – PLC sends signals to output devices like motors, lamps, and valves.]`

### Q8. What is a PLC scan cycle? Why must it repeat continuously? (5 marks)

`[A PLC scan cycle is the process in which the PLC reads inputs processes the program, and updates outputs.
It repeats continuously to monitor and control the machine.Continuous scanning helps the PLC respond quickly to changes in inputs It ensures the automation process works correctly and continuously.]`

### Q9. Identify the PLC section responsible for each function. (4 marks)

| Function | PLC Section |
|---|---|
| Executes the user program | `[CPU]` |
| Stores the program and data | `[Memory]` |
| Reads field-device signals | `[Inout Module]` |
| Controls external devices | `[Output Module]` |

---

## Section C — SCADA Fundamentals (20 marks)

### Q10. Expand SCADA and explain its purpose. (5 marks)

`[SCADA stands for Supervisory Control and Data Acquisition.
It is used to monitor and control industrial processes.
It collects data from machines and sensors.
It displays the data on a computer screen for easy monitoring and control.]`

### Q11. State five important functions of a SCADA system. (5 marks)

1. `[Monitoring – Monitors industrial processes.]`
2. `[Data collection – Collects data from sensors and machines]`
3. `[Control – Controls machines and processes.]`
4. `[Alarm – Gives alerts when problems occur]`
5. `[Data storage – Stores process data for future use.]`


### Q12. Why is SCADA described as the “eyes” of an automation system? (4 marks)

`[SCADA is called the “eyes” of an automation system because it allows operators to see what is happening in the process. It shows real-time data from sensors and machines. It also displays alarms, status, and process values on a computer screen. This helps operators monitor and control the system easily]`
### Q13. Name four industries or services where SCADA can be used. (4 marks)

1. `[Power plants]`
2. `[Water treatment]`
3. `[Oil and gas]`
4. `[Manufacturing industries]`

### Q14. What is the difference between monitoring and controlling? (2 marks)

`[Monitoring: Watching and checking the system status.
Controlling: Giving commands to change or operate the system.]`

---

## Section D — PLC, HMI and SCADA Relationship (15 marks)

### Q15. Complete the comparison table. (9 marks)

| System | Main purpose | Typical user/location | Example task |
|---|---|---|---|
| PLC | `[Controls machines]` | `[Factory / Machine]` | `[Start or stop motor]` |
| HMI | `[Displays and controls process]` | `[Operator station]` | `[Show temperature]` |
| SCADA | `[Monitors and controls processes]` | `[Control room]` | `[Monitor whole plant]` |

### Q16. Explain how information travels from a field sensor to a SCADA screen. (6 marks)

`[Sensor detects a physical value like temperature or pressure.]`
`[The sensor sends the signal to the PLC.]`
`[The PLC processes the signal.]`
`[The data is sent to the SCADA system through a communication network.]`
`[SCADA receives and processes the data.]`
`[The value is displayed on the SCADA screen for the operator.]`

---

## Section E — Industrial Application Challenge (15 marks)

### Scenario: Automatic Water Tank

A tank must fill automatically. A low-level sensor detects when water is low, and a high-level sensor detects when the tank is full. A pump supplies water. The operator should see the tank and pump status on a monitoring screen.

### Q17. Identify the PLC inputs and output. (3 marks)

- Inputs: `[Low-level sensor, High-level sensor]`
- Output: `[Low-level sensor, High-level sensor]`

### Q18. Write the required control behaviour in plain language. (4 marks)

`[When the water level is low, the pump should start.
The pump should continue filling the tank.
When the tank is full, the pump should stop.
The operator should see the tank level and pump status on the monitoring screen.]`

### Q19. State four items that should be visible on the SCADA/HMI screen. (4 marks)

1. `[Tank water level]`
2. `[ItemPump ON/OFF status]`
3. `[High-level alarm]`
4. `[ItemLow-level alarm]`

### Q20. Suggest one alarm and one value/event that should be recorded. (4 marks)

- Alarm: `[High water level alarm]`
- Recorded value/event: `[Pump ON/OFF status and time of operation.]`

---

## Submission Checklist

- [x] I entered my student information.
- [x] I answered Questions 1–20.
- [x] I used my own words.
- [x] I checked spellings and technical terms.
- [x] I completed `student-work/reflection.md`.
- [x] I made at least three meaningful commits.
- [x] I checked the Actions result.
- [x] I submitted my repository link to Prof. Dattaraj Vidyasagar.
