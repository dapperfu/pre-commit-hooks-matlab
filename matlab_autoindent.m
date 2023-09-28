% ChatGPT: Write a MATLAB script to automate opening a matlab file using the editor (doc matlab.desktop.editor). Use the appropriate function to auto indent (Ctrl-I).
% This lead to finding https://github.com/okomarov/TidyCode.

% Define the file path
fileToOpen = 'path/to/your/matlab/file.m';

% Open the file in the MATLAB editor
editorObj = matlab.desktop.editor.openDocument(fileToOpen);

% Check if the document was opened successfully
if ~isempty(editorObj)
    % Perform auto-indentation (Ctrl-I)
    editorObj.smartIndentContents();
    
    % Save the changes (optional)
    % editorObj.save();
    
    % Close the editor (optional)
    % editorObj.close();
else
    fprintf('Failed to open the file: %s\n', fileToOpen);
end
