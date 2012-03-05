# coding: utf-8
#!/usr/bin/env python

from torneira.controller import BaseController
import simplexml

class VideologController(BaseController):
    
    def config(self, request_handler, **kw):
        
        if kw.get("params"):
            ordered_params = ["google_analytics_account", "custom_thumb", "related", "hd", "volume", "color1", "color2", "color3", "source", "link", "scale", "offset_x", "offset_y", "align"]

            params = kw.get("params").split(",")
            for posicao in xrange(0,len(params)):
                kw[ordered_params[posicao]] = params[posicao]
        
        args = {
            'hd' : kw.get('hd', ''),
            'related' : kw.get('related', ''),
            'volume' : kw.get('volume', ''),
            'slideshow' : kw.get('slideshow', ''),
            'theme' : {
                'color1' : kw.get('color3', ''),
                'color2' : kw.get('color2', ''),
                'color3' : kw.get('color1', ''),
            },
            'watermark' : {
                'source' : kw.get('source', ''),
                'link' : kw.get('link', ''),
                'scale' : kw.get('scale', ''),
                'offset_x' : kw.get('offset_x', ''),
                'offset_y' : kw.get('offset_y', ''),
                'align' : kw.get('align', '')
            },
            'custom_thumb' : kw.get('custom_thumb', ''),
            'google_analytics_account' : kw.get('google_analytics_account', ''),
         }

        return self.render_to_xml({'data': args}, request_handler = request_handler)