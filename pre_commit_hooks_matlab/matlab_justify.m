function matlab_justify()
%%
fid = fopen('mfiles.txt', 'r');

while ~feof(fid)
    line = fgetl(fid);
    edit(line)
    editor = matlab.desktop.editor.getActive;
    justify();
    editor.save()
    editor.close()
end