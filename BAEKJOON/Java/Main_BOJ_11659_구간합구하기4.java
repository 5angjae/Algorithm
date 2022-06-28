package com.ktds.step01.array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_BOJ_11659_구간합구하기4 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[] a = new int[N+1];
		int[] sum = new int[N+1];
		
		st = new StringTokenizer(in.readLine(), " ");
		for (int i = 1; i <= N; i++) {
			a[i] = Integer.parseInt(st.nextToken());
			sum[i] = sum[i-1] + a[i];
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(in.readLine(), " ");
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			System.out.println(sum[to]-sum[from-1]);
		}
		
	}

}
