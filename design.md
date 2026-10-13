# Groupwork  Practical Exercise 3: Designing a Searching Agent


## Group members


Ahmed Najma Wanjiku - 192797  [Graph and search tree] [Link]

 
Mureithi Davidtelios -  [PEAS and agent design] [Link]


Mungai Patrick -  [UCS and calculations] [Link] 
## 1. Self-driving trailer as an intelligent agent



### 2.3 Distance measurements

| From | To | Distance (km) |
|---|---|---:|
| Nairobi | Naivasha | 90 |
| Naivasha | Nakuru | 71 |
| Nakuru | Kericho | 108 |
| Kericho | Kisumu | 84 |
| Nairobi | Narok | 142 |
| Narok | Bomet | 81 |
| Bomet | Kericho | 79 |
| Nairobi | Thika | 40 |
| Thika | Nyeri | 110 |
| Nyeri | Nyahururu | 103 |
| Nyahururu | Nakuru | 75 |


### 2.4 Weighted directed graph

```mermaid
flowchart TD
    A["Nairobi"] -->|"90 km"| B["Naivasha"]
    A -->|"142 km"| C["Narok"]
    A -->|"40 km"| D["Thika"]
    B -->|"71 km"| E["Nakuru"]
    C -->|"81 km"| F["Bomet"]
    D -->|"110 km"| G["Nyeri"]
    G -->|"103 km"| H["Nyahururu"]
    H -->|"75 km"| E
    E -->|"108 km"| I["Kericho"]
    F -->|"79 km"| I
    I -->|"84 km"| J["Kisumu"]
```

### 2.5 Search tree of potential routes

.

```mermaid
flowchart TD
    A["Nairobi (0)"]
    A -->|"90"| B["Naivasha (90)"]
    A -->|"142"| C["Narok (142)"]
    A -->|"40"| D["Thika (40)"]
    B -->|"71"| E["Nakuru (161)"]
    E -->|"108"| F["Kericho (269)"]
    F -->|"84"| G["Kisumu (353)"]
    C -->|"81"| H["Bomet (223)"]
    H -->|"79"| I["Kericho (302)"]
    I -->|"84"| J["Kisumu (386)"]
    D -->|"110"| K["Nyeri (150)"]
    K -->|"103"| L["Nyahururu (253)"]
    L -->|"75"| M["Nakuru (328)"]
    M -->|"108"| N["Kericho (436)"]
    N -->|"84"| O["Kisumu (520)"]
    style G fill:#bbf7d0,color:#14532d,stroke:#16a34a
```

## 3. Finding the optimal path



## group photo


