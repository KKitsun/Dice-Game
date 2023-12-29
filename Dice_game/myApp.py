from flask import Flask, render_template, url_for, request, flash, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = ''

game = {
    'f_player': 0,
    's_player' : 0,
    'round': 0,
    'stat': []
}

@app.route("/")
def main_page():
     return render_template('main.html')

@app.route('/start/')
def start():
    game['f_player'] = 0
    game['round'] = 0
    game['s_player'] = 0
    game['stat'] = []
    return render_template('game_page.html', title = 'Dice Game')

@app.route('/roll/')
def roll():
    return redirect(url_for('dice_game'))

@app.route('/game/')
def dice_game():
    import random

    dice_one = None
    dice_two = None

    if game['round'] < 5:
        game['round'] += 1
        
        dice_one = random.randint(1,6)
        dice_two = random.randint(1,6)
        if dice_one > dice_two :
            game['f_player'] += 1
            game['stat'].append(f'{dice_one} > {dice_two}')
            flash('First player won', category='win1')
        elif dice_one < dice_two :
            game['s_player'] += 1
            game['stat'].append(f'{dice_one} < {dice_two}')
            flash('Second player won', category='win2')
        elif dice_one == dice_two :
            game['stat'].append(f'{dice_one} = {dice_two}')
            flash('Draw', category='draw')
    else:
        if game['f_player'] > game['s_player'] :
            flash('First player victory', category='totalwin1')
        elif game['f_player'] < game['s_player'] :
            flash('Second player victory', category='totalwin2')
        elif game['f_player'] == game['s_player'] :
            flash('Draw', category='totaldraw')

    return render_template('game_page.html', dice_one = dice_one, dice_two = dice_two, title = 'Dice Game', game_stat = game['stat'])

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug = True)
