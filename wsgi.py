from tables_visualization import app as application
import webbrowser, random, threading


if __name__ == '__main__':
    #port = 5000 + random.randint(0, 999)
    #url = "http://127.0.0.1:{0}".format(port)
    port=8000
    #url = "http://127.0.0.1:{0}".format(port)
    url = "http://0.0.0.0:{0}".format(port)
    threading.Timer(1.25, lambda: webbrowser.open(url)).start()
    application.run(host='0.0.0.0', port=port, debug=False)
