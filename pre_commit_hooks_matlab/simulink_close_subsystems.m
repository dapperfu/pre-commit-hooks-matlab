function simulink_close_subsystems()
%%

fid = fopen('models.txt', 'r');

while ~feof(fid)
    % Do not save the model if nothing has changed.
    doSave = false;

    % Read each changed model.
    line = fgetl(fid);
    % Split the path and filename apart.
    [path, modelName, ~] = fileparts(line);
    % Change to the model path and open the model.
    cd(path);
    open_system(modelName);

    % Make sure that at least one tab of the model is opened to
    % the root of the model.
    if ~strcmp(bdroot, gcs)
        open_system(bdroot);
        doSave = doSave | true;
    end

    % Close all non-root subsystem tabs.
    openSystems=find_system(bdroot,'MatchFilter',@Simulink.match.allVariants, ...
        'FindAll','on','LookUnderMasks','all',...
        'FollowLinks','on','Open','on');
    openSystems=reshape(openSystems,1,numel(openSystems));
    % Find which models aren't root.
    nonRoot=~strcmp(get(openSystems,'Name'),get(openSystems,'Path'));
    % Close the systems.
    close_system(openSystems(nonRoot));
    % If any non-root subsystems were closed, save the file.
    if any(nonRoot)
        doSave = true;
    end

    if doSave
        % Only save the Simulink model if something has changed.
        % Re-saving an unchanged model changes a few parameters
        % (LastModifiedDate & RTWModifiedTimeStamp) that cause
        % pre-commit to fail as it sees a file change even if nothing has
        % changed in the model itself.
        save_system(modelName);
    end
    % Close the system.
    close_system(modelName);
end