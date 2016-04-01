# Truant Calendar :)

@copyright GradPaul

    The purpose we build this project is for school CREDIT.
    Luckly we made a great team, having fun working togather.

# How to run?

1. Check if config.py is created?
2. If not, run

        cp config-sample.py config.py

3. Adjust config.py specificly bases on your resources location(etc. database).
4. Everything all set, run

        python app.py

5. Server should be up & run, listen at 23300 port.

# Folder usage

```
.
├── cmd
└── server
    ├── static
    │   ├── css
    │   └── images
    │       ├── index
    │       └── result
    ├── templates
    └── views
```


| Folder | Usage |
|:------:|:------|
| cmd | Configurations for installation & building |
| server | Main module |
| static | Place to store static files, etc. css, images |
| templates | The templates to be rendered by __Flask__ |
| views | V in MVC, handle HTML render |
