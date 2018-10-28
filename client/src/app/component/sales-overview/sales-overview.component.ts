import { Component, OnInit, OnDestroy } from '@angular/core';
import { SaleService } from 'src/app/service/sale.service';
import { Subscribable, Subscription } from 'rxjs';
import { Sale } from 'src/app/model/sale.model';
import { MatSnackBar } from '@angular/material';

@Component({
  selector: 'app-sales-overview',
  templateUrl: './sales-overview.component.html',
  styleUrls: ['./sales-overview.component.scss']
})
export class SalesOverviewComponent implements OnInit, OnDestroy {
  displayedColumns: string[] = ['timestamp', 'product', 'amount', 'payment', 'actions'];
  footerColumns: string[] = ['timestamp', 'payment'];
  loading = false;
  sales = [];

  private salesUpdatedSubscription: Subscription;

  constructor(private saleService: SaleService,
              private snackBar: MatSnackBar) { }

  ngOnInit() {
    this.loadSales();

    this.salesUpdatedSubscription = this.saleService.salesUpdated$.subscribe(_ => this.loadSales());
  }

  ngOnDestroy(): void {
    this.salesUpdatedSubscription.unsubscribe();
  }

  loadSales(): void {
    this.loading = true;

    this.saleService.getAll().subscribe(data => {
      this.sales = data;
      this.loading = false;
    });
  }

  deleteSale(sale: Sale) {
    this.saleService.delete(sale).subscribe(_ => {
      this.saleService.notifyUpdate();
    }, error => {
      this.snackBar.open(`Could not delete the sale 🤔 (${error.status})`);
    });
  }

  getTotalCost() {
    return this.sales.map(t => t.payment).reduce((acc, value) => acc + value, 0);
  }
}
