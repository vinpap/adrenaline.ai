// définir une fonction qui prend en paramètres une série de données et affiche un graphique

function plot_graphs(args) {
    let x = args["dates"];
    let y_distance = args["distance"];
    let y_calories = args["calories"]
    var distance_plot_data = [
        {
            x: x,
            y: y_distance,
            type: 'bar',
            name: 'Distance parcourue'
        }
    ];
    var calories_plot_data = [
        {
            x: x,
            y: y_calories,
            type: 'bar',
            name: 'Calories brûlées'
        }
    ];

    var distance_layout = {
        title: 'Distance parcourue (en km)'
    }
    var calories_layout = {
        title: 'Calories brûlées'
    }
    Plotly.newPlot("distance-graph", distance_plot_data, distance_layout);
    Plotly.newPlot("calories-graph", calories_plot_data, calories_layout);
}