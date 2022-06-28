package com.ktds.step01.array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_BOJ_11720_숫자의합 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		String numbers = in.readLine();
		int sum = 0;
		for (int i = 0; i < N; i++) {
			sum += numbers.charAt(i) - 48;
		}
		System.out.println(sum);
	}

}
