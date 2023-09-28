function close_simulink_subsystems()
%%
fid = fopen('models.txt', 'r');

while ~feof(fid)
    line = fgetl(fid);
    [path, filename, ~] = fileparts(line);
    addpath(path);
    closeSubSystems(filename)
end