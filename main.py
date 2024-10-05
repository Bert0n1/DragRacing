import application


app = application.Application((1000,1000), 60)
app.start()
app.main_loop()