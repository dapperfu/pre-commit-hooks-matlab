function matlab_smart_indent()
%%
fid = fopen('mfiles.txt', 'r');

while ~feof(fid)
    line = fgetl(fid);
    edit(line)
    editor = matlab.desktop.editor.getActive;
    [~, filename, ~] = fileparts(editor.Filename);
    smartIndent(filename, 'All');
    editor.save()
    editor.close()
end