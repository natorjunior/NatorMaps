import sqlite3
import pandas as pd
class NatorMaps:
    def __init__(self, db_path,str1="Legenda de cima", str2="de baixo", faixa={1: "Inexistente.",
                  2: "0 &lt; x ≤ 1,4",
                  3: "1,4 &lt; x ≤ 2,8",
                  4: "x &gt; 2,8"}):
        self.db_path = db_path
        self.cabecalho = """<svg version="1.2" viewBox="-41.4233 2.7843 4.1706 5.0733" stroke-linecap="round" stroke-linejoin="round" id="svg2302" inkscape:version="1.1 (c68e22c387, 2021-05-23)" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg">
                    <defs id="defs2306"></defs>
                    <sodipodi:namedview id="namedview2304" pagecolor="#ffffff" bordercolor="#666666" borderopacity="1.0" inkscape:pageshadow="2" inkscape:pageopacity="0.0" inkscape:pagecheckerboard="0" showgrid="false" inkscape:zoom="256" inkscape:cx="3.3203125" inkscape:cy="2.9238281" inkscape:window-width="1920" inkscape:window-height="1017" inkscape:window-x="1912" inkscape:window-y="-8" inkscape:window-maximized="1" inkscape:current-layer="svg2302"></sodipodi:namedview>"""
        self.str1 = str1
        self.str2= str2
        self.faixa = faixa
        self.db_path = "natorMaps.db"

    def __get_municipios(self, uf):
        
        query = "SELECT * FROM municipio WHERE uf == ?"
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (uf,))
            results = cursor.fetchall()
        df = pd.DataFrame(results, columns=[col[0] for col in cursor.description])
        return df
    
    def get_svg(self, uf,cores={}, legenda=False):
        df = self.__get_municipios(uf)
        cor_base = "#838383"
        df.malha_g = df.malha_g.apply(lambda x: x.replace('transform="', f'fill="{cor_base}"'+' stroke="#000" stroke-width="8" transform="'))

        for municipio in df.itertuples():
            if municipio.codigo_ibge in cores:
                df.at[municipio.Index, 'malha_g'] = municipio.malha_g.replace(cor_base, cores[municipio.codigo_ibge])
        if legenda:
            svg = self.cabecalho + df.malha_g.str.cat(sep=' ')+ self._legenda()+ "</svg>"
        else:
            svg = self.cabecalho + df.malha_g.str.cat(sep=' ')+"</svg>"
        return svg
            
    def _legenda(self):
        str1=self.str1
        str2=self.str2
        faixa=self.faixa
        return f"""
  <text xml:space="preserve" style="font-style:normal;font-weight:normal;font-size:0.118114px;line-height:1.25;font-family:sans-serif;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.00345285" x="-38.397652" y="6.3534689" id="text4034-0"><tspan sodipodi:role="line" id="tspan4032-9" x="-38.397652" y="6.3534689" style="stroke-width:0.00345285">{str1}</tspan><tspan sodipodi:role="line" x="-38.397652" y="6.5261116" style="stroke-width:0.00345285" id="tspan4418">{str2}</tspan></text>
  <rect style="fill:#F1F0F0;stroke-width:0.616745" id="rect2410" width="0.19471946" height="0.14135256" x="-38.278282" y="6.6007891"></rect>
  <text xml:space="preserve" style="font-style:normal;font-weight:normal;font-size:0.118114px;line-height:1.25;font-family:sans-serif;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.00345285" x="-38.051498" y="6.7156239" id="text4034"><tspan sodipodi:role="line" id="tspan4032" x="-38.051498" y="6.7156239" style="stroke-width:0.00345285">{faixa[1]}</tspan></text>
  <rect style="fill:#FFE8D6;stroke-width:0.616745" id="rect2410-2" width="0.19471946" height="0.14135256" x="-38.269489" y="6.831069"></rect>
  <text xml:space="preserve" style="font-style:normal;font-weight:normal;font-size:0.118114px;line-height:1.25;font-family:sans-serif;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.00345285" x="-38.042706" y="6.9459038" id="text4034-6"><tspan sodipodi:role="line" id="tspan4032-2" x="-38.042706" y="6.9459038" style="stroke-width:0.00345285">{faixa[2]}</tspan></text>
  <rect style="fill:#FFA366;stroke-width:0.616745" id="rect2410-2-1" width="0.19471946" height="0.14135256" x="-38.265583" y="7.0537252"></rect>
  <text xml:space="preserve" style="font-style:normal;font-weight:normal;font-size:0.118114px;line-height:1.25;font-family:sans-serif;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.00345285" x="-38.038799" y="7.16856" id="text4034-6-5"><tspan sodipodi:role="line" id="tspan4032-2-2" x="-38.038799" y="7.16856" style="stroke-width:0.00345285">{faixa[3]}</tspan></text>
  <rect style="fill:#E85011;stroke-width:0.616745" id="rect2410-2-1-3" width="0.19471946" height="0.14135256" x="-38.257771" y="7.2881002"></rect>
  <text xml:space="preserve" style="font-style:normal;font-weight:normal;font-size:0.118114px;line-height:1.25;font-family:sans-serif;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.00345285" x="-38.030987" y="7.402935" id="text4034-6-5-3"><tspan sodipodi:role="line" id="tspan4032-2-2-6" x="-38.030987" y="7.402935" style="stroke-width:0.00345285">{faixa[4]}</tspan></text>"""