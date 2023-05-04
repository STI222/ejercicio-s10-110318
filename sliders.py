import pandas as pd
import ipywidgets as widgets

# Cargamos los datos del archivo CSV
df = pd.read_csv("random_data.csv")

# Pesos en la villa olimpica
weights = [0.5, 0.8, 0.5, 0.5]

# Creamos un desplegable para seleccionar el jugador
player_dropdown = widgets.Dropdown(options=df['Name'].values, description='Jugador:')

# Creamos los sliders para controlar la importancia de cada característica
soccer_slider = widgets.FloatSlider(value=0.5, min=0.0, max=1.0, step=0.01, description='Soccer')
basketball_slider = widgets.FloatSlider(value=0.5, min=0.0, max=1.0, step=0.01, description='Basketball')
kungfu_slider = widgets.FloatSlider(value=0.5, min=0.0, max=1.0, step=0.01, description='Kungfu')
f1_slider = widgets.FloatSlider(value=0.5, min=0.0, max=1.0, step=0.01, description='F1')

# Creamos una función que actualice los valores de la tabla al cambiar el valor de los sliders o al seleccionar un jugador
def update_table(val):
    # Obtenemos el valor actual del desplegable y los sliders
    player_val = player_dropdown.value
    soccer_val = soccer_slider.value
    basketball_val = basketball_slider.value
    kungfu_val = kungfu_slider.value
    f1_val = f1_slider.value

    # Obtenemos las características del jugador seleccionado y las almacenamos en un vector
    player_features = df.loc[df['Name'] == player_val, 'Soccer':'F1'].values[0]

    # Calculamos el vector de características ajustado según los pesos de los sliders
    weighted_features = player_features * weights

    # Comparamos cada elemento del vector ajustado con el valor del slider correspondiente
    # y actualizamos la columna correspondiente en el DataFrame
    df.loc[df['Name'] == player_val, 'Soccer'] = 1 if weighted_features[0] > soccer_val else 0
    df.loc[df['Name'] == player_val, 'Basketball'] = 1 if weighted_features[1] > basketball_val else 0
    df.loc[df['Name'] == player_val, 'Kungfu'] = 1 if weighted_features[2] > kungfu_val else 0
    df.loc[df['Name'] == player_val, 'F1'] = 1 if weighted_features[3] > f1_val else 0

    # Actualizamos la tabla
    table.value = df.to_html(index=False)

# Creamos la tabla inicial
table = widgets.HTML(value=df.to_html(index=False))

# Actualizamos la tabla al mover los sliders o al seleccionar un jugador
player_dropdown.observe(update_table, 'value')
soccer_slider.observe(update_table, 'value')
basketball_slider.observe(update_table, 'value')
kungfu_slider.observe(update_table, 'value')
f1_slider.observe(update_table, 'value')

# Mostramos el desplegable, los sliders y la tabla
widgets.VBox([player_dropdown, soccer_slider, basketball_slider, kungfu_slider, f1_slider, table])

print("hola")