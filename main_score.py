import utils
from score import get_score


def generate_html_content(body_content):
    return f'''
           <!DOCTYPE html>
           <html>
           <head>
               <title>Dynamic HTML</title>
           </head>
           <body>
               {body_content}
           </body>
           </html>
           '''


def score_body_content(score):
    return f'''
    <h1>The score is:</h1> 
    <div id="score"> {score}</div>'''


def error_body_content():
    return f'''
    <h1>Error:</h1>
    <div id="score" style="color:red"> {utils.BAD_RETURN_CODE}</div>'''


def score_server():
    html_content = ' '
    try:
        score = get_score()
        html_content = generate_html_content(score_body_content(score))
    except Exception as error:
        utils.BAD_RETURN_CODE = error

    if utils.BAD_RETURN_CODE != '':
        html_content = generate_html_content(error_body_content())

    with open('score_games.html', 'w') as file:
        file.write(str(html_content))

    return html_content
