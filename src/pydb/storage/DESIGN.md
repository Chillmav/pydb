┌──────────┬────────┬────────┬───────────────┬────────┬────────┐
│ header   │ slot 0 │ slot 1 │   FREE SPACE  │ row 1  │ row 0  │
└──────────┴────────┴────────┴───────────────┴────────┴────────┘
                                               ← rows grow
                     slots grow →

Page header
├── page type
├── number of slots
├── free_start
└── free_end

slot 0:
    offset = 4070
    length = 26

slot 1:
    offset = 4031
    length = 39