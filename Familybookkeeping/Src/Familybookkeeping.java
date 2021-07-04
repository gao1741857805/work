public class Demo01_Familybookkeeping {
    public static void main(String[] args){

            // 初始化：用户记账金额的初始值设置为10000元
            int balance = 10000;

            // 初始化：显示收支明细时使用的表头信息（将来在表头字符串后面附加表格详细内容）
            String table = "收支\t账户金额\t收支金额\t说    明\n";
            

            // 界面：为了避免用户执行一个菜单项之后就直接退出，所有操作要放在一个死循环中
            // （在测试过程中，还没有编写退出功能，使用Ctrl+c强制结束程序）
            while (true) {

                // 界面：标题
                System.out.println("------家庭收支记账软件------");

                // 界面：菜单选项
                System.out.println("\t\t1 收支明细");
                System.out.println("\t\t2 登记收入");
                System.out.println("\t\t3 登记支出");
                System.out.println("\t\t4 退    出");

                // 界面：提示用户输入菜单项的序号：
                System.out.print("请输入菜单项的序号：");

                // 读取：用户输入的菜单项序号
                char menuSelection = Utility.readMenuSelection();

                // 系统内部运算：根据用户输入的菜单项，执行对应操作
                switch(menuSelection){
                    case '1':

                        System.out.println(table);

                        break;
                    case '2':

                        // 界面：提示用户输入收入金额
                        System.out.print("请输入收入金额：");
                        int income = Utility.readNumber();

                        // 界面：提示用户输入收入说明
                        System.out.print("请输入收入说明：");
                        String incomeDescription = Utility.readString();

                        // 测试：System.out.print("收入金额：" + income + " 收入说明：" + incomeDescription);

                        // 系统内部运算：将收入金额累加到总余额中
                        balance = balance + income;

                        // 系统内部运算：将新的收入明细信息附加到表格中
                        table = table + "收入\t" + balance + "\t\t" + income + "\t\t" + incomeDescription + "\n";

                        System.out.println("已保存收入登记信息");

                        break;
                    case '3':

                        // 界面：提示用户输入支出金额
                        System.out.print("请输入支出金额：");
                        int outcome = Utility.readNumber();

                        // 界面：提示用户输入支出说明
                        System.out.print("请输入支出说明：");
                        String outcomeDescription = Utility.readString();

                        // 测试：System.out.print("支出金额：" + outcome + " 支出说明：" + outcomeDescription);

                        // 系统内部运算：将支持金额从总金额中减去
                        balance = balance - outcome;

                        // 系统内部运算：将新的支出明细信息附加到表格中
                        table = table + "支出\t" + balance + "\t\t" + outcome + "\t\t" + outcomeDescription + "\n";

                        System.out.println("已保存支出登记信息");
                        break;
                    case '4':

                        // 界面：打印信息提示用户输入确认是否退出的字符
                        System.out.print("确认是否退出(Y/N)：");
                        char confirmWord = Utility.readConfirmSelection();

                        // 系统内部运算：如果用户输入的是Y，那么整个程序停止执行即可
                        if (confirmWord == 'Y') {
                            return ;
                        }

                        break;
                }

            }
        }
}
