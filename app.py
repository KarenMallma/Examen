from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
    .card {
      box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
      max-width: 300px;
      margin: auto;
      text-align: center;
      font-family: arial;
    }

    .title {
      color: grey;
      font-size: 18px;
    }

    button {
      border: none;
      outline: 0;
      display: inline-block;
      padding: 8px;
      color: white;
      background-color: #000;
      text-align: center;
      cursor: pointer;
      width: 100%;
      font-size: 18px;
    }

    a {
      text-decoration: none;
      font-size: 22px;
      color: black;
    }

    button:hover, a:hover {
      opacity: 0.7;
    }
    </style>
    </head>
    <body>

    <h2 style="text-align:center">User Profile Card</h2>

    <div class="card">
      <img src="https://alchetron.com/cdn/joe-cole-actor-7f04f55e-0fa5-4e95-858e-3fffec865da-resize-750.jpeg">
      <h1>Karen Mallma</h1>
      <p class="title">Estudiante</p>
      <p>Instituto continental</p>
      <div style="margin: 24px 0;">
        <a href="#"><i class="fa fa-dribbble"></i></a> 
        <a href="#"><i class="fa fa-twitter"></i></a>  
        <a href="#"><i class="fa fa-linkedin"></i></a>  
        <a href="#"><i class="fa fa-facebook"></i></a> 
      </div>
      <p><button>Contact</button></p>
    </div>

    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)