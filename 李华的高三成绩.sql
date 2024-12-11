/*
 Navicat Premium Data Transfer

 Source Server         : py
 Source Server Type    : MySQL
 Source Server Version : 80037
 Source Host           : localhost:3306
 Source Schema         : python

 Target Server Type    : MySQL
 Target Server Version : 80037
 File Encoding         : 65001

 Date: 29/11/2024 00:10:47
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 李华的高三成绩
-- ----------------------------
DROP TABLE IF EXISTS `李华的高三成绩`;
CREATE TABLE `李华的高三成绩`  (
  `考试名称` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `年级排名` int(0) NULL DEFAULT NULL,
  `总分` int(0) NULL DEFAULT NULL,
  `数学` int(0) NULL DEFAULT NULL,
  `语文` int(0) NULL DEFAULT NULL,
  `英语` int(0) NULL DEFAULT NULL,
  `理综` int(0) NULL DEFAULT NULL,
  `考试时间` int(0) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 李华的高三成绩
-- ----------------------------
INSERT INTO `李华的高三成绩` VALUES ('11月联考', 122, 416, 104, 94, 88, 130, 20231123);
INSERT INTO `李华的高三成绩` VALUES ('1月联考', 268, 392, 88, 92, 104, 108, 20230116);
INSERT INTO `李华的高三成绩` VALUES ('3月全市第一次联考', 152, 500, 120, 98, 97, 185, 20240314);
INSERT INTO `李华的高三成绩` VALUES ('9月衡水联考', 270, 394, 100, 85, 83, 127, 20230918);
INSERT INTO `李华的高三成绩` VALUES ('上学期期中考试', 241, 437, 88, 109, 97, 143, 20230126);
INSERT INTO `李华的高三成绩` VALUES ('三校联考', 220, 454, 85, 96, 94, 179, 20240404);
INSERT INTO `李华的高三成绩` VALUES ('江西省十三校联考', 119, 504, 115, 103, 98, 188, 20240503);
INSERT INTO `李华的高三成绩` VALUES ('宜春市二模', 129, 517, 92, 94, 113, 218, 20240419);
INSERT INTO `李华的高三成绩` VALUES ('江西师大附中联考', 137, 485, 110, 87, 102, 186, 20230321);
INSERT INTO `李华的高三成绩` VALUES ('高考', 144, 532, 130, 120, 115, 220, 20240606);
INSERT INTO `李华的高三成绩` VALUES ('宜春市三模', 94, 526, 110, 99, 108, 209, 20240524);

SET FOREIGN_KEY_CHECKS = 1;
