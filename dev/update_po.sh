#!/bin/sh

#############################################################
echo "Generating the pot file..."

echo "    [cli]"
xgettext -L perl -k_T --from-code=UTF-8 --files-from=po/POTFILES_cli.in -o po/template_cli.pot || exit 1

echo "    [gtk]"
xgettext -L perl -k_T --from-code=UTF-8 --files-from=po/POTFILES_gtk.in -o po/template_gtk.pot || exit 1

echo "    [gedit]"
xgettext -L python -k_T --from-code=UTF-8 --files-from=po/POTFILES_gedit.in -o po/template_gedit.pot || exit 1

echo "    [sublime_text2]"
xgettext -L python -k_T --from-code=UTF-8 --files-from=po/POTFILES_sublime_text_2.in -o po/template_sublime_text_2.pot || exit 1

echo "    [gedit3]"
xgettext -L python -k_T --from-code=UTF-8 --files-from=po/POTFILES_gedit3.in -o po/template_gedit3.pot || exit 1

echo "    [config]"
xgettext -L python -k_T --from-code=UTF-8 --files-from=po/POTFILES_config.in -o po/template_config.pot || exit 1

#############################################################
echo "Updating the existing translations..."

echo "    [cli]"
for PO_FILE in po/*/LC_MESSAGES/autolatex.po
do
	msgmerge --backup=none -U "$PO_FILE" "po/template_cli.pot" || exit 1
done

echo "    [gtk]"
for PO_FILE in po/*/LC_MESSAGES/autolatexgtk.po
do
	msgmerge --backup=none -U "$PO_FILE" "po/template_gtk.pot" || exit 1
done

echo "    [gedit]"
for PO_FILE in po/*/LC_MESSAGES/geditautolatex.po
do
	msgmerge --backup=none -U "$PO_FILE" "po/template_gedit.pot" || exit 1
done

echo "    [sublime_text_2]"
for PO_FILE in po/*/LC_MESSAGES/sublime-text-2-autolatex.po
do
	msgmerge --backup=none -U "$PO_FILE" "po/template_sublime_text_2.pot" || exit 1
done

echo "    [gedit3]"
for PO_FILE in po/*/LC_MESSAGES/autolatex-gedit3.po
do
	msgmerge --backup=none -U "$PO_FILE" "po/template_gedit3.pot" || exit 1
done

echo "    [config]"
for PO_FILE in po/*/LC_MESSAGES/autolatex-config.po
do
	msgmerge --backup=none -U "$PO_FILE" "po/template_config.pot" || exit 1
done

