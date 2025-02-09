"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;
const vscode = __importStar(require("vscode"));
const path = __importStar(require("path"));
async function activate(context) {
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
        }
        catch (error) {
            console.error('Ошибка при создании или открытии файла:', error);
        }
    });
    context.subscriptions.push(start_plugin);
}
function deactivate() { }
function extractFunctionName(code) {
    const match = code.match(/^def\s+(\w+)\s*\(/);
    return match ? match[1] : null;
}
function generateTestTemplate(functionName, functionCode) {
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
//# sourceMappingURL=extension.js.map