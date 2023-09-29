% function simulink_zoom_subsystems()

%% 

% Open the list of models passed from pre-commit and corresponding Python
% file.
fid = fopen('models.txt', 'r');

while ~feof(fid)
    % Read each changed model.
    line = fgetl(fid);
    % Split the path and filename apart.
    [path, modelName, ~] = fileparts(line);
    % Add the path and open the model.
    addpath(path);
    open_system(modelName);
    currentSystem = gcs;

    % Do not save the model if nothing has changed.
    doSave = false;

    subSystems = find_system(bdroot, 'FindAll', 'on', 'BlockType', 'SubSystem');

    for subSystem = subSystems'
        open_system(get(subSystem, 'Path'))

        % Set ZoomFactor so the model fits the window.
        zoomBefore = get_param(get(subSystem, 'Path'), 'ZoomFactor');
        set_param(get(subSystem, 'Path'), 'ZoomFactor', 'FitSystem');
        zoomAfter = get_param(get(subSystem, 'Path'), 'ZoomFactor');
        % Only save the file if the ZoomFactor has changed.
        if ~strcmpi(zoomBefore, zoomAfter)
            doSave= doSave | true;
            disp(get(subSystem, 'Path'))
            disp(zoomBefore)
            disp(zoomAfter)
        end
    end

    open_system(currentSystem);
    
    if doSave
        % Only save the Simulink model if something has changed.
        % Re-saving an unchanged model changes a few parameters 
        % (LastModifiedDate & RTWModifiedTimeStamp) that cause
        % pre-commit to fail as it sees a file change even if nothing has
        % changed in the model itself.
        save_system(modelName);
    end

    close_system(modelName);
end