

import cli.CLI;

/**
 * 测试
 *
 * @author wangwei
 * @date 2018/02/05
 */
public class BlockchainTest {

    public static void main(String[] args) {
        try {
           // String[] argss = {"createwallet"};
         //String[] argss = {"createblockchain", "-address", "1HA4KkyRvLpY7UHr7c6mYdMDHZWEdjYaJ1"};
            // 1CceyiwYXh6vL6dLPw6WiNc5ihqVxwYHSA
            // 1G9TkDEp9YTnGa6gS5zaWkwGQwKrRykXcf
            // 1EKacQPNxTd8N7Y83VK11zoqm7bhUZiDHm
          //String[] argss = {"printaddresses"};
          String[] argss = {"getbalance", "-address", "1HA4KkyRvLpY7UHr7c6mYdMDHZWEdjYaJ1"};
           //String[] argss = {"send", "-from", "1HA4KkyRvLpY7UHr7c6mYdMDHZWEdjYaJ1", "-to", "19eq6TGRu5Yj9V5Zu1uBbr1Dh7GziCNtst", "-amount", "1"};
            CLI cli = new CLI(argss);
            cli.parse();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
