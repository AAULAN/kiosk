import { SaleService } from './../../service/sale.service';
import { ProductService } from './../../service/product.service';
import { Component, OnInit } from '@angular/core';
import { Sale } from 'src/app/model/sale.model';
import { Product } from 'src/app/model/product.model';
import { MatSnackBar } from '@angular/material';

@Component({
  selector: 'app-products-overview',
  templateUrl: './products-overview.component.html',
  styleUrls: ['./products-overview.component.scss']
})
export class ProductsOverviewComponent implements OnInit {
  displayedColumns: string[] = ['name', 'price', 'actions'];
  products = [];

  constructor(private productService: ProductService,
              private saleService: SaleService,
              private snackBar: MatSnackBar) { }

  ngOnInit() {
    this.loadProducts();
  }

  loadProducts() {
    this.productService.getAll().subscribe(data => this.products = data);
  }

  purchaseProduct(product: Product) {
    this.saleService.performSale(product).subscribe(data => {
      this.snackBar.open('Sale completed! 🎉');
    }, error => {
      this.snackBar.open(`An error occurred! 😞 (${error.status})`);
    });
  }
}
