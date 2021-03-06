import _plotly_utils.basevalidators


class MapboxValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='mapbox', parent_name='layout', **kwargs):
        super(MapboxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Mapbox'),
            data_docs=kwargs.pop(
                'data_docs', """
            accesstoken
                Sets the mapbox access token to be used for
                this mapbox map. Alternatively, the mapbox
                access token can be set in the configuration
                options under `mapboxAccessToken`.
            bearing
                Sets the bearing angle of the map in degrees
                counter-clockwise from North (mapbox.bearing).
            center
                plotly.graph_objs.layout.mapbox.Center instance
                or dict with compatible properties
            domain
                plotly.graph_objs.layout.mapbox.Domain instance
                or dict with compatible properties
            layers
                plotly.graph_objs.layout.mapbox.Layer instance
                or dict with compatible properties
            layerdefaults
                When used in a template (as
                layout.template.layout.mapbox.layerdefaults),
                sets the default property values to use for
                elements of layout.mapbox.layers
            pitch
                Sets the pitch angle of the map (in degrees,
                where 0 means perpendicular to the surface of
                the map) (mapbox.pitch).
            style
                Sets the Mapbox map style. Either input one of
                the default Mapbox style names or the URL to a
                custom style or a valid Mapbox style JSON.
            uirevision
                Controls persistence of user-driven changes in
                the view: `center`, `zoom`, `bearing`, `pitch`.
                Defaults to `layout.uirevision`.
            zoom
                Sets the zoom level of the map (mapbox.zoom).
"""
            ),
            **kwargs
        )
