import streamlit as st
import streamlit.components.v1 as components
st.markdown('<h1 style="color:white">Beyond Boundaries: Exploring the Data Dynamics of IPL</h1>', unsafe_allow_html=True)

# Paste your Tableau embed code here
embed_code = """
<div class='tableauPlaceholder' id='viz1718202969600' style='position: left'><noscript><a href='#'><img alt='IPL ANALYSIS (2008-2020)) ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ip&#47;ipl_17180442822280&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='ipl_17180442822280&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ip&#47;ipl_17180442822280&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1718202969600');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1575px';vizElement.style.height='719px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1575px';vizElement.style.height='719px';} else { vizElement.style.width='100%';vizElement.style.height='4527px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""
st.components.v1.html(embed_code, width=1570, height=692)


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://www.shutterstock.com/image-vector/night-cricket-stadium-illustration-vector-600nw-2160100275.jpg");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

