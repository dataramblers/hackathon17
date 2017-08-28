<map version="freeplane 1.6.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="Hackathon-Infrastruktur" FOLDED="false" ID="ID_813337702" CREATED="1503932057913" MODIFIED="1503932067024" STYLE="oval">
<font SIZE="18"/>
<hook NAME="MapStyle">
    <properties edgeColorConfiguration="#808080ff,#ff0000ff,#0000ffff,#00ff00ff,#ff00ffff,#00ffffff,#7c0000ff,#00007cff,#007c00ff,#7c007cff,#007c7cff,#7c7c00ff" fit_to_viewport="false"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ICON_SIZE="12.0 pt" COLOR="#000000" STYLE="fork">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10.0 pt" SHAPE_VERTICAL_MARGIN="10.0 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="5" RULE="ON_BRANCH_CREATION"/>
<node TEXT="Flink" POSITION="right" ID="ID_590125386" CREATED="1503932088887" MODIFIED="1503932129480">
<edge COLOR="#ff00ff"/>
<node TEXT="Shared volume f&#xfc;r Index" ID="ID_1731897838" CREATED="1503932312996" MODIFIED="1503932320230"/>
<node TEXT="Als Cluster betreibbar" ID="ID_662263853" CREATED="1503932320695" MODIFIED="1503932419675"/>
</node>
<node TEXT="Elasticsearch" POSITION="right" ID="ID_530263486" CREATED="1503932084182" MODIFIED="1503932088170">
<edge COLOR="#00ff00"/>
<node TEXT="Als Cluster betreibbar" ID="ID_423034693" CREATED="1503932277296" MODIFIED="1503932414450"/>
<node TEXT="Shared volume f&#xfc;r Index" ID="ID_666705938" CREATED="1503932289178" MODIFIED="1503932307268"/>
</node>
<node TEXT="Kafka" POSITION="right" ID="ID_1448261693" CREATED="1503932079259" MODIFIED="1503932858304">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="200" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_280686468" STARTINCLINATION="77;0;" ENDINCLINATION="77;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<edge COLOR="#0000ff"/>
<node TEXT="Als Cluster betreibbar" ID="ID_471176219" CREATED="1503932267986" MODIFIED="1503932408116"/>
</node>
<node TEXT="Metafacture-Runner" POSITION="right" ID="ID_99518023" CREATED="1503932099111" MODIFIED="1503932151264">
<edge COLOR="#00ffff"/>
<node TEXT="Swissbib-Metafacture-Extensions" ID="ID_760386914" CREATED="1503932246654" MODIFIED="1503932254229"/>
</node>
<node TEXT="1" OBJECT="java.lang.Long|1" POSITION="right" ID="ID_280686468" CREATED="1503932070832" MODIFIED="1503934729631">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="200" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_590125386" STARTINCLINATION="153;0;" ENDINCLINATION="153;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="200" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_530263486" STARTINCLINATION="112;0;" ENDINCLINATION="112;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<edge COLOR="#ff0000"/>
<node TEXT="Metafacture-Dependencies" ID="ID_759001241" CREATED="1503932202815" MODIFIED="1503932215965"/>
<node TEXT="Swissbib-Metafacture-Extensions" ID="ID_682327535" CREATED="1503932227083" MODIFIED="1503932234266"/>
<node TEXT="Shared volume f&#xfc;r Notebooks" ID="ID_617404576" CREATED="1503932340703" MODIFIED="1503932347961"/>
<node TEXT="K&#xf6;nnen externe Dependencies geladen werden?" ID="ID_414765470" CREATED="1503932357421" MODIFIED="1503932365947"/>
</node>
</node>
</map>
