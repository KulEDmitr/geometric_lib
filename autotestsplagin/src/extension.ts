import * as vscode from 'vscode';
import * as path from 'path';

export async function activate(context: vscode.ExtensionContext) {
	let start_plugin = vscode.commands.registerCommand('autotestsplagin.createFile', async () => {
		if (!vscode.workspace.workspaceFolders || vscode.workspace.workspaceFolders.length === 0) {
			vscode.window.showWarningMessage('Нет открытого workspace (папки)');
			return;
		}

		const activeEditor = vscode.window.activeTextEditor;
		if (!activeEditor) {
			vscode.window.showWarningMessage('Нет активного файла');
			return;
		}

		const selection = activeEditor.selection;
		const selectedText = activeEditor.document.getText(selection);

		if (selectedText.trim() === '') {
			vscode.window.showWarningMessage('Выделите код функции для переноса.');
			return;
		}

		const functionName = extractFunctionName(selectedText) || "function";

		const testTemplate = generateTestTemplate(functionName, selectedText);

		const filePath = activeEditor.document.uri.fsPath;
		const fileNameWithoutExtension = path.parse(filePath).name;
		const uri = vscode.workspace.workspaceFolders[0].uri;
		const fileUri = vscode.Uri.joinPath(uri, `test_${fileNameWithoutExtension}.py`);

		try {
			await vscode.workspace.fs.writeFile(fileUri, Buffer.from(testTemplate, 'utf-8'));
			const document = await vscode.workspace.openTextDocument(fileUri);
			await vscode.window.showTextDocument(document);
		} catch (error) {
			console.error('Ошибка при создании или открытии файла:', error);
		}
	});

	context.subscriptions.push(start_plugin);
}

export function deactivate() { }

function extractFunctionName(code: string): string | null {
	const match = code.match(/^def\s+(\w+)\s*\(/);
	return match ? match[1] : null;
}

function generateTestTemplate(functionName: string, functionCode: string): string {
	return `import unittest

# Функция, которая будет протестирована 
${functionCode}

class Test${functionName.charAt(0).toUpperCase() + functionName.slice(1)}(unittest.TestCase):
    
    def test_case_1(self):
        # Проверка, что функция возвращает определённое значение
        self.assertEqual(${functionName}(), )

        # Проверка, что функция НЕ возвращает определённое значение
        self.assertNotEqual(${functionName}(), )

        # Проверка булевых значений
        self.assertTrue(${functionName}(), )  # Значение больше 0
        self.assertFalse(${functionName}(), )  # Значение не больше 0
if __name__ == '__main__':
    unittest.main()
	#Чтобы запустить тесты, необходимо прописать команды, python "название файла" или python -m unittest discover
`;
}
