'''
    Provides the templates for the tooltips.
'''


def map_base_hover_template():
    '''
        Sets the template for the hover tooltips on the neighborhoods.

        The label is simply the name of the neighborhood in font 'Oswald'.

        Returns:
            The hover template.
    '''
    # TODO : Generate the hover template
    labelStyle = '<span style="font-family: Oswald">'
    hovertemp = '<br>'.join([labelStyle + ' %{customdata} ' + '<extra></extra>'])
    return hovertemp


def map_marker_hover_template(name):
    '''
        Sets the template for the hover tooltips on the markers.

        The label is simply the name of the walking path in font 'Oswald'.

        Args:
            name: The name to display
        Returns:
            The hover template.
    '''
    # TODO : Generate the hover template
    labelStyle = '<span style="font-family: Oswald">'
    hovertemp = '<br>'.join([labelStyle + name + '<extra></extra>'])
    return hovertemp

def vis2Hover():

    # TODO : Generate the hover template
    labelStyle = '<span style="font-family: Roboto Slab; font-weight:bold">'  # margin-left: 30px
    valueStyle = '<span style="font-family: Roboto; font-weight:regular">'
    closeStyle = '</span>'
    hovertemp = '<br>'.join([
        labelStyle + '          Mortality Rate:' + closeStyle + valueStyle + ' : %{y}' + closeStyle,
        labelStyle + '          Country:' + closeStyle + valueStyle + ' : %{customdata}' + closeStyle   + '<extra></extra>'
    ])
    return hovertemp

def get_heatmap_template():
    template= '%{x} vaccination rate in<br>%{y}: %{customdata} <extra></extra>'
    return template

def get_scatter_template():
    template= '<b>%{customdata}</b><br>vaccination rate: %{y:.0f} %<br>mortality rate: %{x:.0f} %'
    return template